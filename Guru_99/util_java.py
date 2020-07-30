class LoginPage():
    #locator of all element
    text_box_user_id_name="uid"
    text_box_password_name="password"
    click_login_name="btnLogin"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_name(self.text_box_user_id_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_name(self.text_box_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_name(self.click_login_name).click()