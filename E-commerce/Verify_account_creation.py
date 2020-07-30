import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

driver=webdriver.Firefox(executable_path="D:\Edu_Soft\webdriver\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("http://live.demoguru99.com/index.php/")
driver.maximize_window()

driver.find_element_by_xpath("/html/body/div/div/header/div/div[2]/div/a/span[2]").click()
driver.find_element_by_xpath("/html/body/div/div/header/div/div[5]/div/ul/li[1]/a").click()

driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/div/div[1]/div[2]/a").click()

driver.find_element_by_id("firstname").send_keys("Nidhi12354")
driver.find_element_by_id("lastname").send_keys("Khandhediya")
driver.find_element_by_id("email_address").send_keys("sk14253@gmail.com")
driver.find_element_by_id("password").send_keys("Nidhi123")
driver.find_element_by_id("confirmation").send_keys("Nidhi123")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/div[2]/button").click()

driver.find_element_by_xpath("/html/body/div/div/header/div/div[3]/nav/ol/li[2]/a").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[1]/div/div[3]/ul/li[1]/a").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div/div[1]/form[1]/div/div/button[1]/span/span").click()
driver.find_element_by_xpath("//*[@id='email_address']").send_keys("SK@gmail.com")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div/form/div[2]/button").click()