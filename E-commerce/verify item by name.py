import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox(executable_path="D:\Edu_Soft\webdriver\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("http://live.demoguru99.com/index.php/")
driver.maximize_window()

print(driver.title)

titleofwebpage="THIS IS DEMO SITE FOR   "
title =driver.find_element_by_tag_name("h2").text
print(title)

if title == titleofwebpage:
    print("Title verified")
else:
    print("Title not verified")

driver.find_element_by_xpath("/html/body/div/div/header/div/div[3]/nav/ol/li[1]/a").click()
title2 = driver.find_element_by_tag_name("h1").text
print(title2)

element = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/select")
drp=Select(element)
drp.select_by_visible_text("Name")

product_SONY_XPERIA_price=driver.find_element_by_xpath("//*[@id='product-price-1']/span").text
print("product SONY XPERIA price : ",product_SONY_XPERIA_price)

driver.find_element_by_xpath("//*[@id='product-collection-image-1']").click()

detail_SONY_XPERIA_price=driver.find_element_by_xpath("//*[@id='product-price-1']/span").text
print("detail SONY XPERIA price : ",detail_SONY_XPERIA_price)

if product_SONY_XPERIA_price == detail_SONY_XPERIA_price:
    print("both price are equal")
else:
    print("both price are not equal")

driver.find_element_by_xpath("//*[@id='product_addtocart_form']/div[4]/div/div/div[2]/button").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/table/tbody/tr/td[4]/input").clear()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/table/tbody/tr/td[4]/input").send_keys("1000")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/table/tbody/tr/td[4]/button/span/span").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/form/table/tfoot/tr/td/button[2]/span/span").click()

time.sleep(5)