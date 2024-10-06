@Injectable()
export class ProductService {
  constructor(
    @Inject('DB') private db: NodePgDatabase<typeof schema>,
    private readonly commonSerivce: CommonService,
  ) {}

  async findAll(payload: GetProductListReq) {
    const size = payload.size ? payload.size : 10;
    const page = payload.page ? payload.page : 1;

    const offset = (page - 1) * size;

    const totalCountQuery = this.db
      .select({ count: sql<number>`count(${Product.id})::int` })
      .from(Product);

    if (payload.categories) {
      totalCountQuery.leftJoin(Category, eq(Product.category, Category.id));
    }

    const query = this.db
      .select({
        ...selectProduct,
        categories: selectCategories,
        tags: selectTag,
        images: selectImages,
      })
      .from(Product)
      .leftJoin(Category, eq(Product.category, Category.id))
      .leftJoin(ProductTags, eq(ProductTags.productId, Product.id))
      .leftJoin(Tag, eq(ProductTags.tagId, Tag.id))
      .leftJoin(ProductImages, eq(ProductImages.productId, Product.id))
      .leftJoin(Images, eq(ProductImages.images, Images.id));

    const whereOptionsList: SQLWrapper[] = [];

    if (payload.keyword) {
      const keyword = `%${payload.keyword}%`;
      whereOptionsList.push(
        or(ilike(Product.title, keyword), ilike(Product.content, keyword)),
      );
    }
    if (payload.categories) {
      whereOptionsList.push(eq(Category.id, payload.categories));
    }

    const whereOption: SQLWrapper | SQL<unknown> =
      whereOptionsList.length >= 2
        ? and(...whereOptionsList)
        : whereOptionsList[0];

    if (whereOption) {
      query.where(whereOption as SQL);
      totalCountQuery.where(whereOption as SQL);
    }

    query
      .orderBy(asc(Product.createdAt))
      .limit(size)
      .offset(offset)
      .groupBy(Product.id, Category.id);

    const [result, [totalCountResult]] = await Promise.all([
      query,
      totalCountQuery,
    ]);

    const totalPage = Math.ceil(totalCountResult.count / size);
    return { result, totalPage };
  }
}
