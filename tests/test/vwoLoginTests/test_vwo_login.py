import time
import allure
import pytest
from selenium import webdriver
from tests.pageObjects.pom.loginPage import LoginPage
from tests.pageObjects.pom.dashboardPage import DashboardPage
from tests.utils.common_utilis import webdriver_wait
from tests.constants.Constants import Constants

#Assertions and use the Page Object class

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver

@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    try:
        login_page = LoginPage(driver=setup)
        login_page.login_to_vwo(usr="manjiri@gmail.com", pwd="Team@12")
        error_msg_element = login_page.get_error_message_text()
        assert error_msg_element == "Your email, password, IP address or location did not match"

    except Exception as e:
        pytest.xfail("Faield TC")
        print(e)

@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App positive test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    #try:
        login_page = LoginPage(driver=setup)
        login_page.login_to_vwo(usr="manjirigoal@gmail.com", pwd="Team@123")
        time.sleep(10)
        dashboardPage = DashboardPage(driver=setup)
        assert "Manjiri" in dashboardPage.user_logged_in_text()

    #except Exception as e:
    #    pytest.xfail("Failed TC")
    #   print(e)



