from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login page."""

    URL = "https://the-internet.herokuapp.com/login"

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")

    def load(self):
        """Navigate to the login page."""
        self.navigate(self.URL)

    def enter_username(self, username):
        self.find(self.USERNAME_INPUT).clear()
        self.find(self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.find(self.PASSWORD_INPUT).clear()
        self.find(self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.find_clickable(self.LOGIN_BUTTON).click()

    def login(self, username, password):
        """Full login action."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        import time
        time.sleep(2)

    def get_flash_message(self):
        """Return the text of the flash message after login attempt."""
        return self.find(self.FLASH_MESSAGE).text

    def is_logged_in(self):
        """Return True if the logout button is present (i.e. login succeeded)."""
        return self.is_visible(self.LOGOUT_BUTTON, timeout=5)
