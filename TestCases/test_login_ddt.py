import pytest

from PageObjects.Loginpage import Login_page
from Utilities.Readproperties import ReadConfig
from Utilities.CustomeLogger import LogGen
from Utilities import excelutilities
import time
class Test_002_DDT_login:
    baseURL = ReadConfig.getApplicationURL()
    path = "TestData/LoginData.xlsx"
    username = ReadConfig.getUsernamil()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info('**********TEST_002_Login*******')
        self.logger.info('*****Verifying Login DDT Title****')
        self.driver = setup
        self.driver.get(self.baseURL)

        time.sleep(5)
        # So now for this we have to access pageobject class so to use that action method we have to create object of that class
        # through object we can access methods
        #self.lp = Login_page(self.driver)
        # as sson as we create object the consturctor is being called so for that we have to pass parameter
        self.lp = Login_page(self.driver)
        # self.lp = Login_page(self.driver)
        # self.lp.SetUserName(self.username)
        # self.lp.SetPassword(self.password)
        # self.lp.Click_login()
        # self.lp.Click_logout()
        self.logger.info('*****3****')
        #import excelutilities
        self.rows = excelutilities.getRowCount(self.path , 'sheet1')
        #print("the no. of rows", self.rows)
        lst_status = []
        for r in range (2,self.rows+1):
            self.username = excelutilities.readData(self.path,'sheet1',r,1)
            self.password = excelutilities.readData(self.path,'sheet1',r,2)
            self.exp = excelutilities.readData(self.path,'sheet1',r,3)
            self.lp.SetUserName(self.username)
            self.lp.SetPassword(self.password)
            self.lp.Click_login()
            time.sleep(5)
            self.logger.info('*****checking****')
            #self.lp.link_logout_link_text()
        # so after login we can apply login validations successful login or not
        # so just check whetther change in title has been occured or not
            act_tit = self.driver.title
            #print(act_tit)
            exp_title = 'Dashboard / nopCommerce administration'
# self.driver.close()
            if act_tit == exp_title:
                if self.exp == 'pass':
                        self.logger.info("***********test_login passed***************")
                        self.lp.Click_logout()
                        lst_status.append("Pass")
                        ##both title and expected test cases are passed

                    #then we need to append status
                    #When can we say tet_ddt is passed ?
                    #all the combinations should be  passed
                    #so then we can say ddt is passed
                    #so take array is here
                    #if getting as per exp it is being passed
                #so then we have to create an array  and it contains pass so condition must
                    #be like if any fail testcase should be fail
                elif self.exp == "fail":
                        self.logger.info("******failed********")
                        self.lp.Click_logout()
                        lst_status.append("fail")
                        ## 2] when title matching and expected failed
            elif act_tit != exp_title:
                    if self.exp == 'Pass':
                        self.logger.info('***failed****')
                        lst_status.append("Fail")
                        # 3] if title not matching but expecting failed "failed"
                    elif self.exp == "Fail":
                        self.logger.info('****passed*****')
                        lst_status.append('Pass')
                        # 4] if title not matching but expecting failed "failed"

        #after for loop validations will be there
            if "Fail" not in lst_status:
                    self.logger.info("**********login DDT test passed")
                    self.driver.close()
                    assert True
            else:
                    self.logger.info("****login DDT test failed*****")
                    self.driver.close()
                    assert False
                    self.logger.info("****end of Login DDT Test********")
                    self.logger.info('******Completed TC loginDDT _002******')
                # else:
                #     self.driver.save_screenshot(" \\nopcom\\screenshots " + "test_login.png")
                #     self.logger.error('*****failed****')
                #     self.driver.close()
                #     assert False
