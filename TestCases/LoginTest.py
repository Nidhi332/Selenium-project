import time
import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append("D:/Nidhi/TestAutomaiton/pythonUnitTestProject_POMBased")
from PageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    driver=webdriver.Chrome(executable_path="D:/Edu_Soft/chromedriver.exe")

    @classmethod
    def setUpclass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)

        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"Web page title is not match")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/Nidhi/TestAutomaiton/pythonUnitTestProject_POMBased\Reports"))
