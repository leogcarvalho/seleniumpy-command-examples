import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/")

# title
print("O título da página é:", browser.title)

# current_url
print("A URL da página é:", browser.current_url)

# page_source
print("O código-fonte da página é:", browser.page_source)
