from django.conf import settings

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

        soup = BeautifulSoup(page.text, "html.parser")
        products = soup.find_all('span', attrs={'images-two'})

        image_links = []
        image_path = settings.IMAGE_SAVE_PATH
        num = 1
        for tag in products:
            image_links.append(tag.img['data-srcset'])
            link = tag.img['data-srcset']
            name = 'image' + str(num)
            num += 1
            with open(image_path + name + '.jpg', 'wb') as f:
                im = requests.get('https:' + link)
                f.write(im.content)

        output = {
            'url': {
                'link': url,
            },
            'products': {
                'id': 1
            },
        }
        return product_code.PRODUCT_SCRAPE_SUCCESS, output
