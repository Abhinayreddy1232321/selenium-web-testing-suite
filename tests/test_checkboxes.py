import pytest
from pages.checkboxes_page import CheckboxesPage


class TestCheckboxes:
    """
    Test suite for checkbox interaction.
    Target: https://the-internet.herokuapp.com/checkboxes
    Demonstrates: element state validation, user interaction simulation.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = CheckboxesPage(driver)
        self.page.load()

    def test_two_checkboxes_are_present(self):
        """There should be exactly two checkboxes on the page."""
        assert len(self.page.get_checkboxes()) == 2

    def test_first_checkbox_is_unchecked_by_default(self):
        """First checkbox should be unchecked on page load."""
        states = self.page.get_checkbox_states()
        assert states[0] is False

    def test_second_checkbox_is_checked_by_default(self):
        """Second checkbox should be checked on page load."""
        states = self.page.get_checkbox_states()
        assert states[1] is True

    def test_toggle_first_checkbox_to_checked(self):
        """Clicking the first checkbox should mark it as checked."""
        self.page.toggle_checkbox(0)
        states = self.page.get_checkbox_states()
        assert states[0] is True

    def test_toggle_second_checkbox_to_unchecked(self):
        """Clicking the second checkbox should uncheck it."""
        self.page.toggle_checkbox(1)
        states = self.page.get_checkbox_states()
        assert states[1] is False

    def test_toggle_twice_returns_to_original_state(self):
        """Toggling a checkbox twice should restore its original state."""
        original_states = self.page.get_checkbox_states()
        self.page.toggle_checkbox(0)
        self.page.toggle_checkbox(0)
        assert self.page.get_checkbox_states() == original_states
