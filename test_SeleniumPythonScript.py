import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Create a Test Class
class LoginTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path='../drivers/chromedriver')

    @classmethod
    def setUpClass(cls):
        # create a new Webdriver session for Chrome
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        cls.driver.implicitly_wait(30)
        # Navigate to application Home page
        cls.driver.get("https://www.hudl.com/")
        cls.driver.maximize_window()

    def test_valid_login(self):
        # Check for valid Username and password
        try:
            self.setUpClass()
            self.loginLink = self.driver.find_element_by_link_text('Log in')
            self.loginLink.click()
            self.Email = self.driver.find_element_by_id('email')
            self.Email.send_keys('mukati.aarti012@gmail.com')
            self.password = self.driver.find_element_by_id('password')
            self.password.send_keys('malviya123')
            self.loginButton = self.driver.find_element_by_id('logIn')
            self.loginButton.click()
            self.wait = WebDriverWait(self.driver, 30)
            self.element = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hui-globalnav__home-logo')))
        except TimeoutException:
            print('Timed out while waiting for page to load')

    def test_invalid_login(self):
        # Validate error for invalid login credentials
        self.loginLink = self.driver.find_element_by_link_text('Log in')
        self.loginLink.click()
        self.Email = self.driver.find_element_by_id('email')
        self.Email.send_keys('mukati.aarti012@gmail.com')
        self.password = self.driver.find_element_by_id('password')
        self.password.send_keys('malya123')
        self.loginButton = self.driver.find_element_by_id('logIn')
        self.loginButton.click()
        # Verify if the error message is present
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'login-error-container'))
        self.wait = WebDriverWait(self.driver, 10)

    @classmethod
    def tearDown(cls):
        # Quit the driver
        cls.driver.quit()

    def is_element_present(self, how, what):
        # Method for checking the existence of an element
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True


if __name__ == "__main__":
    unittest.main(verbosity=2)
