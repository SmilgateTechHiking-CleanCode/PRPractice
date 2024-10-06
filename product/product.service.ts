@Injectable()
export class ProductService {
  constructor(
    @Inject('DB') private db: NodePgDatabase<typeof schema>,
    private readonly commonSerivce: CommonService,
  ) {}

  async getProductList(payload: GetProductListReq, whereOption: SQL) {
    const size = payload.size ? payload.size : DEFAULT_SIZE;
    const page = payload.page ? payload.page : DEFAULT_PAGE;

    const offset = (page - 1) * size;

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
      .leftJoin(Images, eq(ProductImages.images, Images.id))
      .where(whereOption);

    query
      .orderBy(asc(Product.createdAt))
      .limit(size)
      .offset(offset)
      .groupBy(Product.id, Category.id);

    return query;
  }

  async getTotalPage(payload: GetProductListReq, whereOption: SQL) {
    const size = payload.size ? payload.size : DEFAULT_SIZE;

    const query = this.db
      .select({ count: sql<number>`count(${Product.id})::int` })
      .from(Product);

    if (payload.categories) {
      query.leftJoin(Category, eq(Product.category, Category.id));
    }
    query.where(whereOption);

    const [totalCountResult] = await query;

    const totalPage = Math.ceil(totalCountResult.count / size);
    return totalPage;
  }
  getwhereOptions(payload: GetProductListReq) {
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
    return whereOption as SQL;
  }
}
