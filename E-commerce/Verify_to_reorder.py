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

#click on reorder
driver.find_element_by_link_text("REORDER").click()

#click on edit button
driver.find_element_by_xpath("//*/input[@data-cart-item-id='TV002']/following-sibling::ul/li/a").click()

#Edit
driver.find_element_by_id("qty").clear()
driver.find_element_by_id("qty").send_keys("10")

#click update cart
driver.find_element_by_xpath("//button[@class='button btn-cart']").click()
driver.find_element_by_xpath("//li[@class='method-checkout-cart-methods-onepage-bottom']/button[@class='button btn-proceed-checkout btn-checkout'and @title='Proceed to Checkout']").click()

#click continue button
driver.find_element_by_xpath("//div[@id='billing-buttons-container']/button").click()

time.sleep(10)
#click continue button
driver.find_element_by_xpath("//div[@id='shipping-method-buttons-container']/button").click()


#click payment option
time.sleep(10)
driver.find_element_by_xpath("//input[@id='p_method_checkmo']").click()


#after payment click continue button
driver.find_element_by_xpath("//div[@id='payment-buttons-container']/button").click()

#place order
time.sleep(5)
driver.find_element_by_xpath("//div[@id='review-buttons-container']/button").click()
