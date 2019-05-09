import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By

def wait():
	time.sleep(3)

def get_title_from_product(product):
	titles = product.find_all('div', class_ = 'title')
	return titles[0].a.h5.div.text.strip()

def get_page():
	browser = webdriver.Firefox(executable_path = r'./geckodriver')  
	browser.get('https://www.tottus.cl/tottus/')  
	wait()
	category =  browser.find_element_by_xpath('''//html/body/div[1]/div[1]/div[3]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/section[3]/div[2]/div[2]/a/img''')
	category.click()
	wait()
	webpage = browser.execute_script('''return document.getElementsByTagName('html')[0].innerHTML''')
	soup = bs(webpage, 'html.parser')
	return soup

def get_products(page):
	return page.find_all('div', class_ = 'item-product-caption')

page = get_page()
products = get_products(page)
for product in products:
	title = get_title_from_product(product)
	print title