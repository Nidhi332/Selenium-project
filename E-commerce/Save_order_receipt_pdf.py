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

#click on my order
check=driver.find_element_by_link_text("MY ORDERS").click()

#Check order status == "pending"
status=driver.find_element_by_xpath("//*/em").text
print(status)

time.sleep(5)
#click on view order
driver.find_element_by_link_text("VIEW ORDER").click()

#print order
driver.find_element_by_link_text("Print Order").click()

driver.switch_to_window()

