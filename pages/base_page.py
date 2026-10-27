from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Base class for all page objects. Contains shared helper methods."""

    DEFAULT_TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        """Navigate to a given URL."""
        self.driver.get(url)

    def find(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for an element and return it."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        """Wait for an element to be clickable and return it."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def is_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        """Return True if element is visible within timeout, else False."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_title(self):
        """Return the current page title."""
        return self.driver.title

    def get_url(self):
        """Return the current page URL."""
        return self.driver.current_url
