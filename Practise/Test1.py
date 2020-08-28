from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="D:\Edu_Soft\webdriver\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(3)
countries=driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

print(driver.find_element_by_id("autosuggest").text)
