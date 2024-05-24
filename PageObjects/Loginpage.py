from selenium.webdriver.common.by import By



class Login_page:
    textbox_username_id = 'Email'
    textbox_password_id = 'Password'
    button_login_xpath = '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button'
    link_logout_link_text = 'logout'


    def __init__(self, driver):

        self.driver = driver
#capture driver from tc and pass in self.driver and helps to use in action methods

#below are the action methods
    #before sending keys or data first clear it {clear()}
    # beacause in data driven what happen whatever data you have provided earlier instill present there
    #and again if you have done
    def SetUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def SetPassword(self, Password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(Password)

    def Click_login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def Click_logout(self):
        self.driver.find_element(By.LINK_TEXT ,self.link_logout_link_text).click()
