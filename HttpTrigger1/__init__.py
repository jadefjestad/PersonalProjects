import logging

import azure.functions as func

import pandas as pd
import os

df = pd.read_csv(os.getcwd() + '\\Book1.csv')

csv_read = str(df['a'][1])

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = os.getcwd() + '\\chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://www.bestbuy.ca/en-ca/collection/monitors-on-sale/13061?path=category%253AComputers%2B%2526%2BTablets%253Bcategory%253AMonitors%253Bcurrentoffers0enrchstring%253AOn%2BSale%253Bprice200to1200%253A%2524200%2B-%2B%2524299.99%257C%2524300%2B-%2B%2524399.99%253Bmonitorresolution0enrchstring%253A2560%2Bx%2B1440%257C4K%2BUltra%2BHD%2B%25283840%2Bx%2B2160%2529%253Blcdmonitorscreensize0enrchrange%253A25%2B-%2B29%2Binch%253BsellerName%253ABestBuyCanada')

import time

time.sleep(20)  # this is to get ample time for the page to load

#-----------

h1 = driver.find_elements_by_class_name('productItemName_3IZ3c')

product_names = []
for i in h1:
    product_names.append(i.text)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Name: {name}, {product_names[0]}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
