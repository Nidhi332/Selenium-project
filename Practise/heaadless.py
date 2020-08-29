from selenium import webdriver
import time


chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")



driver = webdriver.Chrome(executable_path="D:\Edu_Soft\webdriver\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
print(driver.title())
