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


# Class for the main page
class HomePageAround:
    # Create a locator for the Occupation field in the user profile
    profile_description = (By.CLASS_NAME, 'profile__description')

    def __init__(self, driver):
        self.driver = driver

    # Wait for the Occupation field to appear
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.profile_description))

    # Retrieve the value of the Occupation field
    def get_description(self):
        return self.driver.find_element(*self.profile_description).text


class TestAround:

    driver = None

    @classmethod
    def setup_class(cls):
        # Create a driver for Chrome
        cls.driver = webdriver.Chrome()

    def test_get_description(self):
        # Open the test application page
        self.driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=en')

        # Create a page object class for the login page
        login_page = LoginPageAround(self.driver)
        # log in
        login_page.login('rafiki1209@gmail.com', 'Rlms1209')

        # Create a page object for the main page
        home_page = HomePageAround(self.driver)
        # Wait for the main page to load
        home_page.wait_for_load_home_page()
        # Save the value of Occupation to description
        description = home_page.get_description()

        # Use assert to check that the actual value of Occupation matches the expected value
        assert description == 'Explorer'

    @classmethod
    def teardown_class(cls):
        # Close the browser
        cls.driver.quit()
