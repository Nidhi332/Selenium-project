import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver=webdriver.Firefox(executable_path="D:\Edu_Soft\webdriver\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("http://live.demoguru99.com/index.php/")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='header']/div/div[2]/div/a").click()
driver.find_element_by_xpath("//*[@id='header-account']/div/ul/li[1]/a").click()
driver.find_element_by_name("login[username]").send_keys("sk14253@gmail.com")
driver.find_element_by_name("login[password]").send_keys("Nidhi123")
driver.find_element_by_id("send2").click()

driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div[2]/ul/li[8]/a").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div/div[1]/form[1]/div/table/tbody/tr/td[5]/div/button").click()
#driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[3]/div/ul/li[1]/button").click()
#driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div/div[1]/form[1]/div/table/tbody/tr/td[5]/div/button/span/span").click()

time.sleep(10)

Country_element= driver.find_element_by_xpath("//*[@id='country']")
drp=Select(Country_element)
drp.select_by_visible_text("India")

driver.find_element_by_id("region").send_keys("Gujarat")
driver.find_element_by_id("postcode").send_keys("123456")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[3]/div/ul/li[1]/button/span/span").click()

driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/ol/li[1]/div[2]/form/div/div/button").click()
time.sleep(10)
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/ol/li[3]/div[2]/form/div[3]/button").click()

time.sleep(10)
button=driver.find_element_by_xpath("//*[@id='dt_method_checkmo']/input")
driver.execute_script("arguments[0].click();", button)

driver.find_element_by_xpath("//*[@id='payment-buttons-container']/button").click()
time.sleep(5)
#place order
driver.find_element_by_xpath("//*[@id='checkout-review-submit']/div/button").click()