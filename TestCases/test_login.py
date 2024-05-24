import pytest
from selenium import webdriver
from PageObjects.Loginpage import Login_page
from Utilities.Readproperties import ReadConfig
from Utilities.CustomeLogger import LogGen
import time
class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsernamil()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepage_title(self):

    # as soon as  we launch our page the homepage title should match...so for that this testcase
        self.logger.info('**********TEST_001_Login*******')
        self.logger.info('*****Verifying home page Title****')
        self.driver = webdriver.chrome()
        # self.driver =
        self.driver.get(self.baseURL)
        time.sleep(5)
        act_title = self.driver.title


        if act_title == 'Your store. Login':
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot("\\.nopcom\\screenshots" + "test_homepagetitle.png")
            self.logger.error('*****failed****')
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)

        # So now for this we have to access pageobject class so to use that action method we have to create object of that class
        # through object we can access methods
        #self.lp = Login_page(self.driver)
        # as sson as we create object the consturctor is being called so for that we have to pass parameter
        self.lp = Login_page(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassword(self.password)
        self.lp.Click_login()
        time.sleep(5)

        # so after login we can apply login validations successful login or not
        # so just check whetther change in title has been occured or not
        act_tit = self.driver.title

        # self.driver.close()

        if act_tit == 'Dashboard / nopCommerce administration':
            self.logger.info("***********test_login passed***************")
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(" \\nopcom\\screenshots " + "test_login.png")
            self.logger.error('*****failed****')
            self.driver.close()
            assert False
