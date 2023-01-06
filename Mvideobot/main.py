import requests
import json
from config import headers, cookies
import os
import math
import sqlite3


def get_data(catagory_type = 5427):

    params = {
        'categoryId': catagory_type,
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    if not os.path.exists('data'):
        os.mkdir('data')

    s = requests.Session()

    response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()

    total_items = response.get('body').get('total')

    if total_items is None:
        return '[!] No items'

    pages_count = math.ceil(total_items / 24)

    print(f'[INFO] Total positions: {total_items} | Total pages: {pages_count}')

    products_ids = {}
    products_description = {}
    products_prices = {}

    for i in range(pages_count):
        offset = f'{i * 24}'

        params = {
            'categoryId': catagory_type,
            'offset': offset,
            'limit': '24',
            'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
            'doTranslit': 'true',
        }

        response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                                headers=headers).json()

        products_ids_list = response.get('body').get('products')

        products_ids[i] = products_ids_list

        json_data = {
            'productIds': products_ids_list,
            'mediaTypes': [
                'images',
            ],
            'category': True,
            'status': True,
            'brand': True,
            'propertyTypes': [
                'KEY',
            ],
            'propertiesConfig': {
                'propertiesPortionSize': 5,
            },
            'multioffer': True,
        }

        response = s.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

        products_description[i] = response

        products_ids_str = ','.join(products_ids_list)

        params = {
            'productIds': products_ids_str,
            'addBonusRubles': 'true',
            'isPromoApplied': 'true',
        }

        response = s.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

        material_prices = response.get('body').get('materialPrices')

        for item in material_prices:
            item_id = item.get('price').get('productId')
            item_base_price = item.get('price').get('basePrice')
            item_sale_price = item.get('price').get('salePrice')
            item_bonus = item.get('bonusRubles').get('total')

            products_prices[item_id] ={
                'item_basePrice': item_base_price,
                'item_salePrice': item_sale_price,
                'item_bonus': item_bonus
            }

        print(f'[+] Finished {i + 1} of the {pages_count} pages')

    with open('data/1_product_ids.json', 'w', encoding='utf-8') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    with open('data/2_product_description.json', 'w', encoding='utf-8') as file:
        json.dump(products_description, file, indent=4, ensure_ascii=False)

    with open('data/3_product_prices.json', 'w', encoding='utf-8') as file:
        json.dump(products_prices, file, indent=4, ensure_ascii=False)


def get_result():
    result = []

    db = sqlite3.connect('products.db')
    c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS products (
        productId text,
        productLink text,
        basePrice integer,
        salePrice integer,
        productBonus integer
    )""")

    db.commit()

    with open('data/2_product_description.json', encoding='utf-8') as file:
        products_data = json.load(file)

    with open('data/3_product_prices.json', encoding='utf-8') as file:
        products_prices = json.load(file)

    for items in products_data.values():
        products = items.get('body').get('products')

        for item in products:
            product_id = item.get('productId')

            if product_id in products_prices:
                prices = products_prices[product_id]

            item['item_basePrice'] = prices.get('item_basePrice')
            item['item_salePrice'] = prices.get('item_salePrice')
            item['item_bonus'] = prices.get('item_bonus')
            item['item_link'] = f'https://www.mvideo.ru/products/{item.get("nameTranslit")}-{product_id}'

            c.execute("INSERT INTO products VALUES(?, ?, ?, ?, ?)", (product_id, item['item_link'], item['item_basePrice'], item['item_salePrice'], item['item_bonus']))

    db.commit()

    with open('data/4_result.json', 'w', encoding='utf-8') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

    with open('data/4_result.json', encoding='utf-8') as file:
        result_data = json.load(file)

    for items in result_data.values():
        results = items.get('body').get('products')

        for item in results:
            product_id = item.get('productId')
            product_name = item.get('name')
            product_link = item.get('item_link')
            product_basePrice = item.get('item_basePrice')
            product_salePrice = item.get('item_salePrice')
            product_bonus = item.get('item_bonus')
            result.append(
                {
                'id': product_id,
                'name': product_name,
                'link': product_link,
                'basePrice': product_basePrice,
                'salePrice': product_salePrice,
                'bonus': product_bonus
                }
            )

    with open('data/5_bot_res.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

def main():
    get_data()
    get_result()

if __name__ == '__main__':
    main()