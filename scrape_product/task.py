# from celery.decorators import task
import os

import requests
from bs4 import BeautifulSoup
from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings

logger = get_task_logger(__name__)


@shared_task(name='product_scraping')
def product_scraping(url):
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
        try:
            with open(image_path + name + '.jpg', 'wb') as f:
                im = requests.get('https:' + link)
                f.write(im.content)
        except FileNotFoundError:
            os.mkdir(image_path)
            with open(image_path + name + '.jpg', 'wb') as f:
                im = requests.get('https:' + link)
                f.write(im.content)

    return 'first_task_done'
