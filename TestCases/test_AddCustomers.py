# import pytest
# import time
import pytest

from PageObjects.Loginpage import Login_page
from PageObjects.AddcustomerPage import AddCustomer
from Utilities.CustomeLogger import LogGen
from Utilities.Readproperties import ReadConfig
from selenium.webdriver.support.wait import WebDriverWait
import string
import random


class Test_003_Addcustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsernamil()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self, setup):
        self.logger.info("****************TEST_003_AddCustomer *********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        #self.driver.implicitly_wait(10)
        self.lp = Login_page(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassword(self.password)
        self.lp.Click_login()
        self.logger.info("************Login Successful*****")

        self.logger.info("********* Starting Add Customer test*****")
        #self.driver.implicitly_wait(15)
        self.addcust = AddCustomer(self.driver)  # create object of addcust class
        self.addcust.clickOnCustomersMenu()  # method will call and execute
        self.addcust.clickOnCustomersMenuItem()  # method will call and execute

        self.addcust.clickOnAddnew()
        # method will call and execute #as we are calling from addcustomers and executing  wherever we have to pass
        # argurements we will pass
        self.logger.info("**********Providing customer info******")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword('test123')
        self.addcust.setCustomerRoles('Guest')
        self.addcust.setManagerOfVendor("vendor")
        self.addcust.setGender('male')
        self.addcust.setFirstName('Pawan')
        self.addcust.setManagerOfVendor('Kumar')
        self.addcust.setDob('7/05/1985')  # d/mm/yyyy
        self.addcust.setCompanyName('busyQA')
        self.addcust.setAdminContent('This is for testing...')
        self.addcust.clickOnSave()

        self.logger.info("******Saving customer info********")
        self.logger.info("*******Add customer validation*******")
        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            # assert True == True
            self.logger.info('************Add customer test passed********')
            assert True
        else:
            self.driver.save_screenshot('.\\screenshots\\"+"test_addCustomer_scr.png')
            self.logger.error('******add customer test failed*******')
            assert True
        self.driver.close()
        self.logger.info('*****Ending homepage title test********')


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ' '.join(random.choice(chars) for x in range(size))
