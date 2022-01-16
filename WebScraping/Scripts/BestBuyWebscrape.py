# TODO:
#   - setup wait until element found


import os
from dotenv import load_dotenv
import time
import helpmewebscrape
import pandas as pd
from datetime import datetime

load_dotenv()
print(".env loaded? " + os.getenv('LOAD_TEST'))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = 'C:/Users/Jade/webdriver/chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://www.bestbuy.ca/en-ca/collection/monitors-on-sale/13061?path=category%253AComputers%2B%2526%2BTablets%253Bcategory%253AMonitors%253Bcurrentoffers0enrchstring%253AOn%2BSale%253Bprice200to1200%253A%2524200%2B-%2B%2524299.99%257C%2524300%2B-%2B%2524399.99%253Bmonitorresolution0enrchstring%253A2560%2Bx%2B1440%257C4K%2BUltra%2BHD%2B%25283840%2Bx%2B2160%2529%253Blcdmonitorscreensize0enrchrange%253A25%2B-%2B29%2Binch%253BsellerName%253ABestBuyCanada')

#-----------

time.sleep(20)  # this is to get ample time for the page to load

#-----------

h1 = driver.find_elements_by_class_name('productItemName_3IZ3c')

product_names = []
for i in h1:
    product_names.append(i.text)

df_new = pd.DataFrame (product_names, columns = ['ProductNames'])
df_new['DateTime'] = str(datetime.now())

#-----------

df_old = pd.read_csv('WebScraping/Data/ProductNamesNew.csv')

if df_old['ProductNames'].tolist() != df_new['ProductNames'].tolist():
    print('there is a change in on the page')
    df_replace = pd.read_csv('WebScraping/Data/ProductNamesNew.csv')
    df_replace.to_csv('WebScraping/Data/ProductNamesOld.csv', index=False)
    df_new.to_csv('WebScraping/Data/ProductNamesNew.csv', index=False)

    number_of_new_items=0
    message = '''\
Subject: MONITOR CHANGE (Best Buy)\n\nNew items on page:\n'''
    print("New items on page:")
    for i in df_new['ProductNames'].tolist():
        # print('Test:' + str(i))
        if i not in df_old['ProductNames'].tolist():
            message += i + '\n'
            print(i)
            number_of_new_items += 1

    print("Sent Text?" + str(helpmewebscrape.send_email('\ \nSubject: MONITOR CHANGE (Best Buy)\nHey! There are {} new monitors on Best Buy. Check your email for details'.format(number_of_new_items), 
        sender_email=os.getenv('EMAIL_SENDER'), 
        password=os.getenv('PASSWORD_EMAIL'), 
        receiver_email=os.getenv('EMAIL_RECEIVER_MOBILE'))))

    print("Sent Email?" + str(helpmewebscrape.send_email(message, 
        sender_email=os.getenv('EMAIL_SENDER'), 
        password=os.getenv('PASSWORD_EMAIL'), 
        receiver_email=os.getenv('EMAIL_RECEIVER'))))

else:
    print('No change on page')

#---------

os.system('pip freeze > ../requirements.txt')    # recreates the requirements.txt file