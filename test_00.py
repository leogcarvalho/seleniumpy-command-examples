import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(12)
browser.maximize_window()
browser.get("https://chercher.tech/practice/frames")

frame1 = browser.find_element(By.ID, "frame1")
browser.switch_to.frame(frame1)
browser.find_element(By.XPATH, "//*[@id='topic']/following-sibling::input").send_keys("escrevendo no iframe1")

frame3 = browser.find_element(By.ID, "frame3")
browser.switch_to.frame(frame3)
checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']")
checkbox.click()

browser.switch_to.default_content()
frame2 = browser.find_element(By.ID, "frame2")
browser.switch_to.frame(frame2)
dropdown_animals = Select(browser.find_element(By.XPATH, "//select[@id='animals']"))
dropdown_animals.select_by_value("babycat")

time.sleep(10)
