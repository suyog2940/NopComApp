import time
import pytest
from PageObjects.Loginpage import Login_page
from PageObjects.SearchCustomerPage import SearchCustomer
from PageObjects.AddcustomerPage import AddCustomer
from Utilities.Readproperties import ReadConfig
from Utilities.CustomeLogger import LogGen

class Test_case_005_SearchCustByname_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsernamil()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByName(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login_page()
        self.lp.SetUserName(self.username)
        self.lp.SetPassword(self.password)
        self.lp.Click_login()
        self.logger.info('******login successful testcase005')
        self.logger.info('******Starting Search Customer By Name*****')

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("*****searching customer by name******")
        searcustomer = SearchCustomer(self.driver)
        searcustomer.setFirstName('victoria')
        searcustomer.clickserach()
        time.sleep(10)
        status = searcustomer.searchCustomerByName('victoria')
        assert  True == status
        self.logger.info('*****TC__004 finished')