from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="D:\Edu_Soft\webdriver\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()
    
driver.close()