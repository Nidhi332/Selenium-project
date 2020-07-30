import time
import HtmlTestRunner
from selenium import webdriver
import unittest
from Guru_99.util_java import LoginPage
from Guru_99 import XLUtils

class LoginTest(unittest.TestCase):

    baseURL="http://www.demo.guru99.com/V4/"
    driver = webdriver.Firefox(executable_path="D:\Edu_Soft\webdriver\geckodriver-v0.26.0-win64\geckodriver.exe")


    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        path = "D:/Nidhi/TestAutomaiton/Selenium/Guru_practise.xlsx"
        rows = XLUtils.getRowCount(path, "Sheet1")
        for r in range(2, rows + 1):
            username = XLUtils.readData(path, "Sheet1", r, 1)
            password = XLUtils.readData(path, "Sheet1", r, 2)
            lp=LoginPage(self.driver)
            lp.setUserName(username)
            lp.setPassword(password)
            lp.clickLogin()
            time.sleep(5)
            try:
                self.driver.switch_to.alert.accept()
                print("test failed")
                XLUtils.writeData(path, "Sheet1", r, 3, "test failed")
            except :
                if self.driver.title == "Guru99 Bank Manager HomePage":
                    print("test is passed")
                    XLUtils.writeData(path, "Sheet1", r, 3, "test passed")
                    manager_id=self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[3]/td").text
                    print(manager_id)
                    self.driver.find_element_by_link_text("Log out").click()
                    self.driver.switch_to.alert.accept()
                    time.sleep(5)
            time.sleep(10)

        @classmethod
        def tearDownClass(cls):
            cls.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/Nidhi/TestAutomaiton/pythonUnitTestProject_POMBased/Guru_report"))