import BaseTest


# !!! Do not create your own WebDriver. !!!
#
# You can copy credentials from here:
#  - login@codility.com    password
#  - unknown@codility.com  password


# code challenge https://app.codility.com/c/feedback/87GWG3-PZ6/ Abhishek Srivastav Sr. Technical Recruiter asrivastav@arrowcore.com M:- 678-400-0101
class LoginPageTest(BaseTest.BaseTest):
    # 1
    def testLoginFormPresent(self):
        # below you can find already setup webDriver as self.driver
        # email fld and password fld are here on the page
        email_fld = self.driver.find_element_by_id("email-input")
        assert len(str(email_fld.text)) == 0

        pswd_fld = self.driver.find_element_by_id("password-input")
        assert len(str(pswd_fld.text)) == 0

    # 2
    def test_empthFldVld(self):
        email_fld = self.driver.find_element_by_id("email-input")
        # assert email_fld == len(email_fld.text) # is not None #
        value_email_fld = email_fld.get_attribute('value')
        assert value_email_fld == ''

        pswd_fld = self.driver.find_element_by_id("password-input")
        # assert pswd_fld == len(pswd_fld.text) # is not None
        value_pswd_fld = email_fld.get_attribute('value')
        assert value_pswd_fld == ''

    # 3
    def test_wrngCrdntls(self):
        email_fld = self.driver.find_element_by_id("email-input")
        email_fld.clear()
        email_fld.send_keys("unknown@codility.com")

        pswd_fld = self.driver.find_element_by_id("password-input")
        pswd_fld.clear
        pswd_fld.send_keys('unknown@codility.com')

        lgn_btn = self.driver.find_element_by_id("login-button")
        lgn_btn.click()

        err_msg = self.driver.find_element_by_id("messages")
        assert "You shall not pass! Arr!" == err_msg.text

    # 4
    def test_emlsVldtd(self):
        email_fld = self.driver.find_element_by_id("email-input")
        email_fld.clear()
        email_fld.send_keys("unknowncodility.com")
        pswd_fld = self.driver.find_element_by_id("password-input")
        pswd_fld.clear
        pswd_fld.send_keys('qwerty')
        lgn_btn = self.driver.find_element_by_id("login-button")
        lgn_btn.click()

        err_msg = self.driver.find_element_by_id("messages")
        assert "Enter a valid email" == err_msg.text

    # 5
    def test_rghtCrdntls(self):
        # from selenium.webdriver.support.ui import WebDriverWait
        # from selenium.webdriver.support import expected_conditions as EC
        # from selenium.webdriver.common.by import By
        # from selenium import webdriver

        email_fld = self.driver.find_element_by_id("email-input")
        email_fld.clear()
        email_fld.send_keys("login@ncodility.com")

        pswd_fld = self.driver.find_element_by_id("password-input")
        pswd_fld.clear
        pswd_fld.send_keys('password')
        lgn_btn = self.driver.find_element_by_id("login-button")
        lgn_btn.click()

        # WLCM_MSG = (By.XPATH, "//div[@class='message success']")
        wlcm_msg = self.driver.find_element_by_id("container") # wait.until(EC.visibility_of_element_located(WLCM_MSG))
        assert "Welcome to Codility" == wlcm_msg.text