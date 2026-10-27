from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    """Page object for the checkboxes demo page."""

    URL = "https://the-internet.herokuapp.com/checkboxes"

    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def load(self):
        self.navigate(self.URL)

    def get_checkboxes(self):
        """Return all checkbox elements."""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.CHECKBOXES)
        )

    def get_checkbox_states(self):
        """Return a list of booleans for each checkbox's checked state."""
        return [cb.is_selected() for cb in self.get_checkboxes()]

    def toggle_checkbox(self, index):
        """Toggle checkbox at the given index (0-based)."""
        self.get_checkboxes()[index].click()
