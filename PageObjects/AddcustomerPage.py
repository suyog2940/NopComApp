# import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
#
# class AddCustomer:
#     #lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
#     lnkCustomers_menu_xpath = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
#
#     #lnkCustomers_menu_item_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
#     lnkCustomers_menu_item_xpath = "/html[1]/body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]"
#     #btn_add_new_Xpath = "//a[2class='btn bg blue"
#     btn_add_new_Xpath = "/html[1]/body[1]/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
#
#     txtEmail_xpath = "//input[@id='Email']"
#     txtPassword_xpath = "/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[2]/div[2]/div[1]/input[1]"
#     #txtPassword_xpath = "//input[@id = 'Password']"
#     #txtFirstName_xpath = "//input[@id ='firstName']"
#     txtFirstName_xpath = "/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[3]/div[2]/input[1]"
#     txtLastName_xpath = "/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[4]/div[2]/input[1]"
#     #txtLastName_xpath = "//input[]@id='LastName']"
# #radio buttons
#     rdMaleGender_id = "Gender_male"
#     rdFemaleGender_id = "Gender _Female"
#
#     txtDob_xpath = "//input[@id='DateOfBirth']"
#     txtCompanyName_xpath = "//input[@id='Company']"
#     txtCustomerRoles_xpath = "//div[@class='k.multiselect-wrap k-floatwrap']"
#  #following are the roles
#     lstitemAdministrators_xpath = "//li[contains(text(),'Adminstrators')]"
#     lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
#     lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
#     lstitemVendors_Xpath =  "//li[contains(text(),'vendors')]"
#
#     drpmgOfVendor_xpath = "//*[@id='VendorId']"
#     txtAdminContent_xpath = "//textarea[@id='AdminComment']"
#     btnSave_xpath = "//button[@name='save']"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def clickOnCustomersMenu(self):
#         self.driver.find_element(By.XPATH , self.lnkCustomers_menu_xpath).click()
#
#     def ClickOnCustomersMenuItem(self):
#         self.driver.find_element(By.XPATH , self.lnkCustomers_menu_item_xpath).click()
#
#     def clickOnAddnew(self):
#         self.driver.find_element(By.XPATH ,self.btn_add_new_Xpath).click()
#
#     def SetEmail(self,email):
#         self.driver.find_element(By.XPATH , self.txtEmail_xpath).send_keys(email)
#
#     def setPassword(self,password):
#         self.driver.find_element(By.XPATH , self.txtPassword_xpath).send_keys(password)
#
#     def setCustomerRoles(self,role):
#         self.driver.find_element(By.XPATH , self.txtCustomerRoles_xpath).click()
#         time.sleep(3)
#         if role =='registered':
#             self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
#         elif role == 'Adminstrators':
#             self.listitem = self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
#
#         elif role == 'guests':
#             # here user can be registered or guest ,only one
#             time.sleep(3)
#             #self.driver.find_element(By.XPATH,'//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
#             self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/span/span[1]/span/ul/li[1]/span').click()
#             self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
#
#         elif role == 'registered':
#             self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
#
#         elif role == 'vendors':
#             self.listitem = self.driver.fid_eleemnt(By.XPATH , self.lstitemVendors_Xpath)
#
#         else:
#             self.listitem = self.driver.find_element(By.XPATH , self.lstitemGuests_xpath)
#         time.sleep(3)
#         #self.listitemm.click();
#         self.driver.execute_script("arguments[0].click()",self.listitem)
#
#     def setManagerOfVendor(self,value):
#         drp = Select(self.driver.find_element(By.XPATH , self.drpmgOfVendor_xpath))
#         drp.select_by_visible_text(value)
#     def setGender(self,gender):
#         if gender == 'male':
#             self.driver.find_element(By.ID,self.rdMaleGender_id).click()
#
#         elif gender == 'Female':
#             self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
#         else:
#             self.driver.find_element(By.ID,self.rdMaleGender_id).click()
#
#     def setFirstName(self , fname):
#         self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)
#
#     def setLastName(self , lname):
#         self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)
#
#     def setdob(self,dob):
#         self.driver.find_element(By.XPATH,self.txtDob_xpath).send_keys(dob)
#
#     def setCompanyName(self,comname):
#         self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)
#
#     def setAdminContent(self,content):
#         self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).click()
#
#     def clickOnsave(self):
#         self.driver.find_element(By.XPATH , self.btnSave_xpath).click()


#**********************************************************************************************************

import time
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class AddCustomer:
    # Add customer Page
    #lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_menu_xpath = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
    #lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    time.sleep(2)
    lnkCustomers_menu_item_xpath = "/html[1]/body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]"
    #btnAddnew_xpath = "//a[@class='btn bg-blue']"

    txtPassword_xpath = "/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[2]/div[2]/div[1]/input[1]"
    #     #txtPassword_xpath = "//input[@id = 'Password']"
    #     #txtFirstName_xpath = "//input[@id ='firstName']"
    txtFirstName_xpath = "/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[3]/div[2]/input[1]"
    txtLastName_xpath = "/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[4]/div[2]/input[1]"

    btn_add_new_Xpath = "/html[1]/body[1]/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    txtEmail_xpath = "//input[@id='Email']"
    #txtPassword_xpath = "//input[@id='Password']"
    #txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    txtcustomerRoles_xpath = "//li[@title='Registered']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemRegistered_css_selector = "#select2-SelectedCustomerRoleIds-result-ubv6-3"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    #drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    drpmgrOfVendor_xpath = "(//li[@id='select2-SelectedCustomerRoleIds-result-5wog-5'])[1]"
    drpmgrOfVendor_css_selector = "//li[@id='select2-SelectedCustomerRoleIds-result-5wog-5']" #"select2-SelectedCustomerRoleIds-result-5wog-5"
    drpmgrOfVendor_id = "select2-SelectedCustomerRoleIds-result-5wog-5" #"select2-SelectedCustomerRoleIds-result-5wog-5"

    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    #txtFirstName_xpath = "//input[@id='FirstName']"
    #txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_item_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.btn_add_new_Xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.list_item = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath) #lstitemRegistered_css_selector
        elif role=='Administrators':
            self.list_item = self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
        elif role=='Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.list_item = self.driver.find_elements(By.XPATH,self.lstitemGuests_xpath)
            if role=='Registered':
                self.list_item = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
            elif role == 'Vendors':
                self.list_item = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
            else:
                self.list_item = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.list_item)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.ID,self.drpmgrOfVendor_id))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.ffind_element(By.ID,self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH,self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        #self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(content)
        self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(content)
    def clickOnSave(self):
        #self.driver.find_element(By.XPATH,self.btnSave_xpath).click()
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()