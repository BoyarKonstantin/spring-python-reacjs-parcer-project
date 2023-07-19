from bs4 import BeautifulSoup
import pandas as pd 
import csv
import psycopg2
import requests
import datetime
from postgres_api import ParcerPostgresAPI

postgres_api_cursor = ParcerPostgresAPI()

class Parcers:
    def ebayParcer(self, url):

        items = []
        headers = {
            "User-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        }

        reqSession = requests.Session()
        req = reqSession.get(url=url, headers=headers)
        src = req.text

        #print(src)
        soup = BeautifulSoup(src, "lxml")
        all_products = soup.find_all("div", class_="s-item__info clearfix")
        
        shop_name = "Ebay"
        today = f'{datetime.date.today()}'
        dumping_status = False
        i = 0
        
        for product in all_products:
            i += 1
            product_name = product.find("h3", class_="s-item__title")
            product_price = product.find("span", class_="s-item__price")
            product_available = "In available"
            product_a = product.next_element
            item = i, product_name.text, product_price.text, product_available, product_a.text, shop_name, today, dumping_status
            items.append(item)
            print(item)


        postgres_api_cursor.post_items(items)

        return items

if __name__ == "__main__":
    parcer = Parcers()
    parcer.ebayParcer("https://www.ebay.co.uk/b/Apple-Mobile-Smartphones/9355/bn_449685?LH_ItemCondition=1000%7C1500&rt=nc&_udlo=280&mag=1")
    