from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DynamicPage(BasePage):
    """Page object for the dynamic loading / search demo pages."""

    URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

    # Locators
    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    LOADING_SPINNER = (By.ID, "loading")
    FINISH_TEXT = (By.CSS_SELECTOR, "#finish h4")

    def load(self):
        """Navigate to the dynamic loading page."""
        self.navigate(self.URL)

    def click_start(self):
        """Click the Start button to trigger dynamic content load."""
        self.find_clickable(self.START_BUTTON).click()

    def get_finish_text(self):
        """Wait for and return the dynamically loaded finish text."""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element(self.FINISH_TEXT, "Hello World!")
        )
        return self.find(self.FINISH_TEXT, timeout=5).text

    def is_spinner_gone(self):
        """Return True once the loading spinner disappears."""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.LOADING_SPINNER)
        )
        return True
