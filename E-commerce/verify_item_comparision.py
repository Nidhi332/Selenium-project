import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox(executable_path="D:\Edu_Soft\webdriver\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("http://live.demoguru99.com/index.php/")
driver.maximize_window()

driver.find_element_by_xpath("/html/body/div/div/header/div/div[3]/nav/ol/li[1]/a").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/div/div[3]/ul/li[2]/a").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[2]/div/div[3]/ul/li[2]/a").click()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[3]/div[1]/div[2]/div/button/span/span").click()

main_page = driver.current_window_handle

for handle in driver.window_handles:
    if handle != main_page:
        compare_page=handle

driver.switch_to.window(compare_page)
time.sleep(10)
driver.close()
driver.switch_to_window(main_page)
#driver.find_element_by_xpath("/html/body/div/div[2]/button/span/span").click()

