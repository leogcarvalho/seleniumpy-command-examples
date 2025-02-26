import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://chercher.tech/practice/frames")

iframe1 = browser.find_element(By.ID, "frame1")
browser.switch_to.frame(iframe1)
browser.find_element(By.XPATH, "//*[@id='topic']/following-sibling::input").send_keys("iframe1")
time.sleep(3)

iframe3 = browser.find_element(By.ID, "frame3")
browser.switch_to.frame(iframe3)
checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']")
checkbox.click()
time.sleep(3)

browser.switch_to.default_content()

iframe2 = browser.find_element(By.ID, "frame2")
browser.switch_to.frame(iframe2)
dropdown_animals = Select(browser.find_element(By.XPATH, "//select[@id='animals']"))
dropdown_animals.select_by_value("babycat")
time.sleep(3)



