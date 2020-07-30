import time
import csv

from selenium import webdriver

driver=webdriver.Firefox(executable_path="D:\Edu_Soft\webdriver\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("http://live.demoguru99.com/index.php/backendlogin")
driver.maximize_window()
driver.implicitly_wait(5)

#login with cred
driver.find_element_by_id("username").send_keys("user01")
driver.find_element_by_id("login").send_keys("guru99com")
driver.find_element_by_class_name("form-button").click()

time.sleep(5)
#close pop-up
driver.find_element_by_link_text("close").click()

#select file format as csv(comma seprated value)
driver.find_element_by_id("customerGrid_export").send_keys("csv")

#click on export button
driver.find_element_by_xpath("//button[@title='Export']/span/span/span").click()

time.sleep(5)

path="C:/Users/sagar/AppData/Local/Temp/Cu.csv"

with open(path, mode='rt') as file:
    csv_data = csv.reader(file)
    for row in csv_data:
        print(row)