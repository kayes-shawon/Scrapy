import os

import requests
import ulid
from bs4 import BeautifulSoup
from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings

from scrape_product.models import ProductImage

logger = get_task_logger(__name__)


@shared_task(name='product_scraping')
def product_scraping(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")
    products = soup.find_all('span', attrs={'images-two'})

    product_image = []
    image_path = settings.IMAGE_SAVE_PATH

    for tag in products:
        image_id = ulid.new().str
        link = 'https:' + tag.img['data-srcset']
        image_size = '300px'
        alt_data = tag.img['alt']
        product_url = image_path + 'image' + image_id + '.jpg'
        product_image.append(
            ProductImage(scrape_url=url, product_url=product_url, original_url=link,
                         original_size=image_size, alt_data=alt_data)
        )
        try:
            with open(product_url, 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
        except FileNotFoundError:
            os.mkdir(image_path)
            with open(product_url, 'wb') as f:
                im = requests.get(link)
                f.write(im.content)

    ProductImage.objects.bulk_create(product_image)
    return 'image scraping task done'
