import pytest
from pages.login_page import LoginPage


class TestLogin:
    """
    Test suite for login functionality.
    Target: https://the-internet.herokuapp.com/login
    Valid credentials: tomsmith / SuperSecretPassword!
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = LoginPage(driver)
        self.page.load()

    def test_page_title_is_correct(self):
        """Verify the login page has the correct title."""
        assert "The Internet" in self.page.get_title()

    def test_valid_login_redirects_to_secure_page(self):
        """Valid credentials should redirect to the secure area."""
        self.page.login("tomsmith", "SuperSecretPassword!")
        assert "secure" in self.page.get_url()

    def test_valid_login_shows_success_message(self):
        """Valid login should display a success flash message."""
        self.page.login("tomsmith", "SuperSecretPassword!")
        message = self.page.get_flash_message()
        assert "You logged into a secure area" in message

    def test_valid_login_shows_logout_button(self):
        """After valid login, a logout button should be visible."""
        self.page.login("tomsmith", "SuperSecretPassword!")
        assert self.page.is_logged_in()

    def test_invalid_username_shows_error(self):
        """Wrong username should display an error flash message."""
        self.page.login("wronguser", "SuperSecretPassword!")
        message = self.page.get_flash_message()
        assert "Your username is invalid" in message

    def test_invalid_password_shows_error(self):
        """Wrong password should display an error flash message."""
        self.page.login("tomsmith", "wrongpassword")
        message = self.page.get_flash_message()
        assert "Your password is invalid" in message

    def test_empty_credentials_shows_error(self):
        """Submitting empty fields should display an error message."""
        self.page.login("", "")
        message = self.page.get_flash_message()
        assert "invalid" in message.lower()

    def test_invalid_login_stays_on_login_page(self):
        """Failed login should keep the user on the login page."""
        self.page.login("baduser", "badpass")
        assert "login" in self.page.get_url()
