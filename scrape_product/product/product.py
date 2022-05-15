from scrape_base.base.api import BasePostAPI
from scrape_product.code import product as product_code


class ScrapeProductAPI(BasePostAPI):
    def api_version(self) -> str:
        return 'v1'

    def api_name(self) -> str:
        return 'ScrapeProductAPI'

    def process(self) -> tuple:
        output = {
            'url': {
                'link': "www.bata.com",
            },
            'products': {
                'id': 1
            }
        }
        return product_code.PRODUCT_SCRAPE_SUCCESS, output
