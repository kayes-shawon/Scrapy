from scrape_base.base.api import BasePostAPI
from scrape_product.code import product as product_code

from scrape_product.task import product_scraping


class ScrapeProductAPI(BasePostAPI):
    def api_version(self) -> str:
        return 'v1'

    def api_name(self) -> str:
        return 'ScrapeProductAPI'

    def process(self) -> tuple:
        url = self.api_payload().get('scrape_url')
        product_scraping.delay(url)
        output = {
            'url': {
                'link': url,
            },
            'products': {
                'id': 1
            },
        }
        return product_code.PRODUCT_SCRAPE_SUCCESS, output
