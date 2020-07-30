import time

from selenium import webdriver

driver=webdriver.Firefox(executable_path="D:\Edu_Soft\webdriver\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("http://live.demoguru99.com/index.php/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//*[@id='header']/div/div[2]/div/a").click()
driver.find_element_by_xpath("//*[@id='header-account']/div/ul/li[1]/a").click()
driver.find_element_by_name("login[username]").send_keys("sk14253@gmail.com")
driver.find_element_by_name("login[password]").send_keys("Nidhi123")
driver.find_element_by_id("send2").click()

#click on MOBILE
driver.find_element_by_link_text("MOBILE").click()

#click on add to cart
driver.find_element_by_xpath("//a[@title='IPhone']//parent::h2[@class='product-name']//following-sibling::div[@class='actions']/button").click()

#input coupon code
driver.find_element_by_id("coupon_code").send_keys("GURU50")

#click on apply coupon button
driver.find_element_by_xpath("//input[@id='coupon_code']//parent::div[@class='field-wrapper']/div/button").click()

