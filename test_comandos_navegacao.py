import time
from selenium import webdriver

browser = webdriver.Chrome()

# maximize_window()
browser.maximize_window()

# get()
browser.get("https://google.com")

# refresh()
browser.refresh()

# get()
browser.get("https://www.saucedemo.com/")
time.sleep(2)

# back()
browser.back()
time.sleep(3)

# forward()
browser.forward()
time.sleep(3)

# browser.switch_to.new_window("tab")
# time.sleep(3)
#
# # close()
# browser.close()
# time.sleep(3)

# quit()
browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
time.sleep(3)
browser.quit()
