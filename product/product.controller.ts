@Controller('products')
export class ProductController {
  constructor(private readonly productService: ProductService) {}

  @Get('')
  findAll(@Query() payload: GetProductListReq) {
    return this.productService.findAll(payload);
  }
}
