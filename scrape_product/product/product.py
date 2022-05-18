from bs4 import BeautifulSoup

from scrape_base.base.api import BasePostAPI
from scrape_product.code import product as product_code
import requests


class ScrapeProductAPI(BasePostAPI):
    def api_version(self) -> str:
        return 'v1'

    def api_name(self) -> str:
        return 'ScrapeProductAPI'

    def process(self) -> tuple:
        url = self.api_payload().get('scrape_url')
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser")
        images = [img for img in soup.findAll('img')]
        print(str(len(images)) + " images found.")
        print([i for i in images])
        image_links = [each.get('src') for each in images]
        output = {
            'url': {
                'link': url,
            },
            'products': {
                'id': 1
            },
        }
        return product_code.PRODUCT_SCRAPE_SUCCESS, output
