from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

clear = lambda: os.system('cls')
clear()

browser.get('http://preev.com/')

browser.implicitly_wait(1)

def a():
    return browser.find_element_by_xpath('//*[@id="numField"]').get_attribute('value')

try:
    price = a()
except:
    sleep(2)
    price = a()

files = open('price.txt','w')
files.write(price)
files.close()

print(f'BTC price now : {price}')

browser.quit()