import pytest
from pages.dynamic_page import DynamicPage


class TestDynamicLoading:
    """
    Test suite for dynamic/asynchronous content loading.
    Target: https://the-internet.herokuapp.com/dynamic_loading/1
    Demonstrates: explicit waits, handling async UI behaviour.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = DynamicPage(driver)
        self.page.load()

    def test_page_loads_successfully(self):
        """Page should load without errors."""
        assert "The Internet" in self.page.get_title()

    def test_start_button_is_present(self):
        """Start button should be visible before interaction."""
        assert self.page.is_visible(self.page.START_BUTTON)

    def test_dynamic_content_loads_after_click(self):
        """Clicking Start should eventually reveal 'Hello World!' text."""
        self.page.click_start()
        finish_text = self.page.get_finish_text()
        assert "Hello World!" in finish_text

    def test_spinner_disappears_after_load(self):
        """The loading spinner should disappear once content is loaded."""
        self.page.click_start()
        assert self.page.is_spinner_gone()
