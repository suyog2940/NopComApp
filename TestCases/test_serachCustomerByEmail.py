import time
import pytest
from PageObjects.Loginpage import Login_page
from PageObjects.AddcustomerPage import AddCustomer
from PageObjects.SearchCustomerPage import SearchCustomer
from Utilities.Readproperties import ReadConfig
from Utilities.CustomeLogger import LogGen

class Test_searchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsernamil()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info('******SearchCustomerByEmail_004*****')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp =Login_page(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassword(self.password)
        self.lp.Click_login()
        self.logger.info("*******Login_Succesful*****")
        self.logger.info('******Starting Search Customer By Email*****')

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("*****searching customer by emailId******")
        searcustomer = SearchCustomer(self.driver)
        searcustomer.setEmail('victoria_victoria@nopCommerce.com')
        searcustomer.clickserach()
        time.sleep(10)
        status = searcustomer.searchCustomerbyemail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info('*****TC__004 finished')