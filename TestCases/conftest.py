
import pytest
from selenium import webdriver
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()

    elif browser == 'firefox':
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        driver = webdriver.Chrome()

    return driver
# #
# def pytest_addpotion(parser): #this will get the value from CLI/hooks
#     parser.addoption('--browser')

def pytest_addoption(parser,):
    # default_value = pluginmanager.hook.pytest_config_file_default_value()
    parser.addoption(
        "--browser",
        #help="Config file to use, defaults to %(default)s",
        #default=default_value,
        )
@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver
#**********************************************

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# from selenium.webdriver.chrome.options import Options


# In pytest, hook functions are functions that can be used to extend or
# modify the behavior of pytest. They are called automatically by pytest at
# specific times during the test run.

# The pytest_configure function is a hook function in pytest that is called once the
# configuration object has been created and all plugins and initial conftest files have been loaded.

# The pytest_addoption function is a hook function in pytest that is used to add custom command-line options to the
# pytest command. It takes a single argument, parser, which is an instance of the argparse.ArgumentParser class.


# add arg --broswer this for your command linner
# def pytest_addoption(parser):
#     parser.addoption("--browser")
# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser', action='store', default='edge', help='Base URL for the API tests')
#
#                                                                             # passing the value to --browser
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

# Define the browser fixture function with a single argument, request.
# Within the browser function, use the request.config.getoption() method to get the value
# of the --browser option passed to pytest on the command line.


# here we are passing actual value to --browser
# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         print("Launching Chrome Browser")
#         driver = webdriver.Chrome()
#     elif browser == 'firefox':
#         print("Launching Firefox Browser")
#         driver = webdriver.Firefox()
#     elif browser == 'edge':
#         print("Launching Edge Browser")
#         driver = webdriver.Edge()
#     # if browser == 'headless':
#     else:
#         print("Headless mode")
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("headless")
#         driver = webdriver.Chrome(options= chrome_options)
#         #driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver  #
#     driver.quit()
#
#
def pytest_metadata(metadata):
    metadata["Project Name"] = "NopCom"
    metadata["Environment"] = "QA Environment"
    metadata["Module"] = "User Profile"
    metadata["Tester"] = "Vaibhav"
    metadata.pop("Plugins", None)


# @pytest.fixture(params=[
#
#     ("TestUser101@credence.in", "Test123", "Pass"),
#     ("TestUser101@credence.in1", "Test123", "Fail"),
#     ("TestUser101@credence.in", "Test1231", "Fail"),
#     ("TestUser101@credence.in1", "Test1231", "Fail")
#
# ])
# def getDataForLogin(request):
#     return request.param
# pytest: error: unrecognized arguments: --chrome
# pytest: error: unrecognized arguments: --chrome
# pytest -s -v -n=2 --html=Reports\report.html TestCases/test_login.py
# pytest -s -v -n=2 --alluredir="Allure reports" TestCases/test_login.py
# Allure reports
# pytest -v -s -n=5 --alluredir="Allure reports"  allure serve D:\NopCom\Allure reports


# generate
# html
# reports
# update
# conftest, py


# hook for adding environment info in html reports
#
# def pytest_configure(config):
#     config.metadata['Project name'] = 'nopcommerce'
#     config.metadata['module name'] = 'customers'
#     config.metadata['tester'] = 'suyog'

#
# # It is hook for delete/modify environement info to html reports
#
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_home", None)
#     metadata.pop("plugins", None)
# #pytest -s -v -n=3 --html=path tc path
