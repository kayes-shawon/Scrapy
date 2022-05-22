from scrape_base.base.code import CodeObject

PRODUCT_SCRAPE_SUCCESS = CodeObject(
    http_status=201,
    state_code='SCRAPY_PSS_201'
)

REQUEST_SUCCESSFUL = CodeObject(
    http_status=200,
    state_code='SCRAPY_RS_201'
)

PRODUCT_DOES_NOT_EXIST = CodeObject(
    http_status=404,
    state_code="SCRAPY_PDE_404"
)

NO_QUERY_PROVIDED = CodeObject(
    http_status=400,
    state_code='SCRAPY_NQP_400'
)
