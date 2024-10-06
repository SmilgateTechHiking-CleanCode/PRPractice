@Controller('products')
export class ProductController {
  constructor(private readonly productService: ProductService) {}

  @Get('')
  async getProductListAndTotalPage(@Query() payload: GetProductListReq) {
    const whereOption: SQL = this.productService.getwhereOptions(payload);
    const getTotalPagePromise = this.productService.getTotalPage(
      payload,
      whereOption,
    );
    const findAllPromise = this.productService.getProductList(payload, whereOption);

    const [result, totalPage] = await Promise.all([
      findAllPromise,
      getTotalPagePromise,
    ]);

    return { result, totalPage };
  }
}
