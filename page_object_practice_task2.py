from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Class for the login page
class LoginPageAround:
    email_field = (By.ID, 'email')
    password_field = (By.ID, 'password')
    sign_in_button = (By.CLASS_NAME, 'auth-form__button')

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()


# Class for the header
class HeaderPageAround:
    # Create a locator for the Email element in the header
    header_user = header_user = (By.CLASS_NAME, 'header__user')

    def __init__(self, driver):
        self.driver = driver

    # Wait for the page to load
    def wait_for_load_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.header_user))

    # Method to retrieve the text of the element in the header
    def email_in_header(self):
        return self.driver.find_element(*self.header_user).text


# Class with the autotest
class TestAround:

    driver = None

    @classmethod
    def setup_class(cls):
        # Create a driver for Chrome
        cls.driver = webdriver.Chrome()

    def test_check_email_in_header(self):
        # Open the test application page
        self.driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=en')

        # Create a page object class for the login page
        login_page = LoginPageAround(self.driver)
        # log in
        email = "rafiki1209@gmail.com"
        password = "Rlms1209"
        # Pass these variables to the method
        login_page.login(email, password)

        # Create an object for the header
        header_page = HeaderPageAround(self.driver)
        # Wait for the header to load
        header_page.wait_for_load_header()
        # Retrieve the text of an element in the header
        email_from_header = header_page.email_in_header()

        # Check that the retrieved value matches email
        assert email_from_header == email

    @classmethod
    def teardown_class(cls):
        # Close the browser
        cls.driver.quit()
