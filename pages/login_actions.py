import time
from framework.logger import log_action, setup_logger
from pages.login import LoginPage


class LoginPageActions:

    def __init__(self, login_page: LoginPage):
        """
        Initialize LoginPageActions with a LoginPage instance

        Args:
            login_page: LoginPage object instance
        """
        if not isinstance(login_page, type(login_page)):
            # Just check it has the expected methods
            required_methods = [
                "is_username_input_visible",
                "is_password_input_visible",
                "username_input",
                "password_input",
                "login_button",
                "error_message",
            ]
            for method in required_methods:
                if not hasattr(login_page, method):
                    raise AttributeError(f"LoginPage must have '{method}' attribute")

        self._page = login_page
        self._logger = login_page._logger

    @log_action("Performing login")
    def login(
        self, username: str, password: str, wait_after_login: float = 2.0
    ) -> bool:
        """
        Perform login with username and password

        Args:
            username: Username or email
            password: Password
            wait_after_login: Time to wait after clicking login button (seconds)

        Returns:
            True if login was successful, False otherwise

        Raises:
            Exception: If login fails with details
        """
        try:
            self._logger.info(f"Starting login with username: {username}")

            # Check if inputs are visible
            if not self._page.is_username_input_visible():
                raise AssertionError("Username input not visible")

            if not self._page.is_password_input_visible():
                raise AssertionError("Password input not visible")

            # Enter credentials
            self._logger.debug("Entering username")
            self._page.username_input.send_keys(username)

            self._logger.debug("Entering password")
            self._page.password_input.send_keys(password)

            # Click login button
            self._logger.debug("Clicking login button")
            self._page.login_button.click()

            # Wait for page to process login
            time.sleep(wait_after_login)

            self._logger.info("Login completed successfully")
            return True

        except Exception as e:
            self._logger.error(f"Login failed: {type(e).__name__}: {str(e)}")
            raise
    
    @log_action("Logout")
    def _logout(
        self,
    ) -> bool:
        self._logger.debug("Logout start")
        if self._page.burger.is_visible():
            self._page.burger.click()
        if self._page.is_logout_displayed():
            self._page.logout.click()
            self._logger.debug("SAY: Bye-bye!")


    @log_action("Entering username")
    def enter_username(self, username: str) -> None:
        """
        Enter username without password

        Args:
            username: Username or email to enter
        """
        try:
            if not self._page.is_username_input_visible():
                raise AssertionError("Username input not visible")

            self._logger.debug(f"Entering username: {username}")
            self._page.username_input.send_keys(username)

        except Exception as e:
            self._logger.error(f"Failed to enter username: {e}")
            raise

    @log_action("Entering password")
    def enter_password(self, password: str) -> None:
        """
        Enter password without username

        Args:
            password: Password to enter
        """
        try:
            if not self._page.is_password_input_visible():
                raise AssertionError("Password input not visible")

            self._logger.debug("Entering password")
            self._page.password_input.send_keys(password)

        except Exception as e:
            self._logger.error(f"Failed to enter password: {e}")
            raise

    @log_action("Clicking login button")
    def click_login_button(self) -> None:
        """Click the login button"""
        try:
            if not self._page.is_login_button_clickable():
                raise AssertionError("Login button not clickable")

            self._logger.debug("Clicking login button")
            self._page.login_button.click()

        except Exception as e:
            self._logger.error(f"Failed to click login button: {e}")
            raise

    @log_action("Checking if username input is visible")
    def is_username_input_visible(self) -> bool:
        """Check if username input is visible"""
        try:
            return self._page.is_username_input_visible()
        except Exception as e:
            self._logger.error(f"Failed to check username visibility: {e}")
            return False

    @log_action("Checking if password input is visible")
    def is_password_input_visible(self) -> bool:
        """Check if password input is visible"""
        try:
            return self._page.is_password_input_visible()
        except Exception as e:
            self._logger.error(f"Failed to check password visibility: {e}")
            return False

    @log_action("Checking if login page is displayed")
    def is_page_displayed(self) -> bool:
        """Check if login page is displayed"""
        try:
            return self._page.is_page_displayed()
        except Exception as e:
            self._logger.error(f"Failed to check page display: {e}")
            return False

    @log_action("Checking if error message is displayed")
    def is_error_message_displayed(self) -> bool:
        """Check if error message is displayed"""
        try:
            return self._page.is_error_message_displayed()
        except Exception as e:
            self._logger.error(f"Failed to check error message: {e}")
            return False

    @log_action("Getting error message")
    def get_error_message(self) -> str:
        """Get error message text if displayed"""
        try:
            return self._page.get_error_message()
        except Exception as e:
            self._logger.error(f"Failed to get error message: {e}")
            return None

    @log_action("Clicking forgot password link")
    def click_forgot_password(self) -> None:
        """Click the forgot password link"""
        try:
            self._logger.debug("Clicking forgot password link")
            self._page.forgot_password_link.click()

        except Exception as e:
            self._logger.error(f"Failed to click forgot password: {e}")
            raise

    @log_action("Clicking sign up link")
    def click_sign_up(self) -> None:
        """Click the sign up link"""
        try:
            self._logger.debug("Clicking sign up link")
            self._page.sign_up_link.click()

        except Exception as e:
            self._logger.error(f"Failed to click sign up: {e}")
            raise


    @log_action("Taking screenshot")
    def screenshot(self, file_name: str = "login_page.png") -> None:
        """Take a screenshot of the login page"""
        try:
            self._page.screenshot(file_name)
            self._logger.info(f"Screenshot saved: {file_name}")
        except Exception as e:
            self._logger.error(f"Failed to take screenshot: {e}")
            raise

    @log_action("Validating login form")
    def validate_login_form(self) -> bool:
        """
        Validate that all login form elements are present and visible

        Returns:
            True if all elements are valid, False otherwise
        """
        try:
            checks = {
                "Username input visible": self._page.is_username_input_visible(),
                "Password input visible": self._page.is_password_input_visible(),
                "Login button clickable": self._page.is_login_button_clickable(),
            }

            all_valid = all(checks.values())

            for check_name, result in checks.items():
                status = "✓" if result else "✗"
                self._logger.info(f"{status} {check_name}: {result}")

            return all_valid

        except Exception as e:
            self._logger.error(f"Validation failed: {e}")
            return False
