from bs4 import BeautifulSoup
import pandas as pd 
import csv
import psycopg2
import requests
import datetime


def postgres(items):
    try:
        conn = psycopg2.connect("dbname='parcerDB' user='postgres' host='localhost' password='postgres' connect_timeout=1 ")
    except:
        print("Connection failed")
        return False
    cursor = conn.cursor()
    sql_delete_quety = """
        DELETE FROM parcer_model
    """
    cursor.execute(sql_delete_quety)
    sql_insert_query = """
                        INSERT INTO parcer_model (id,
                        model_name, 
                        price, 
                        available, 
                        model_link,  
                        shop_name, 
                        date, 
                        dumping_status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    """
    result = cursor.executemany(sql_insert_query, items)
    conn.commit()

    print(cursor.rowcount, "Record inserted successfully into mobile table")
    cursor.close()
    conn.close()
    print("PostgreSQL connection is closed")


def parcer(url):

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
        item = i, product_name.text, product_price.text.replace("£", ''), product_available, product_a.text, shop_name, today, dumping_status
        items.append(item)
        print(item)
        
    return items

if __name__ == "__main__":

    items = parcer("https://www.ebay.co.uk/b/Fiction-Non-Fiction-Books/261186/bn_450928")
    postgres(items)
    