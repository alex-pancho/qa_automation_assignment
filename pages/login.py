from dataclasses import dataclass
from framework.locator import Locator, LocatorType, DriverType
from framework.element import element, WebElement
from framework.logger import log_action
from pages._base import BasePage


@dataclass
class LoginPageLocators:
    """All locators for the login page"""

    # Main form
    LOGIN_FORM = Locator(
        type=LocatorType.XPATH,
        value='//div[@class="form_column"]',
    )

    # Input fields
    USERNAME_INPUT = Locator(type=LocatorType.XPATH, value="//*[@id='user-name']")

    PASSWORD_INPUT = Locator(type=LocatorType.XPATH, value="//*[@id='password']")

    # Buttons
    LOGIN_BUTTON = Locator(type=LocatorType.XPATH, value="//*[@id='login-button']")

    ERROR_MESSAGE = Locator(type=LocatorType.XPATH, value="//h3[@data-test='error']")


class LoginPage(BasePage):
    """Page Object Model for Login Page"""

    def __init__(
        self,
        driver,
        driver_type: DriverType = DriverType.SELENIUM,
        timeout: int = 10000,
    ):
        super().__init__(driver, driver_type, timeout)
        self._locators = LoginPageLocators()

    # Elements as properties
    @element("LOGIN_FORM")
    def login_form(self) -> WebElement:
        """Get login form"""
        pass

    @element("USERNAME_INPUT")
    def username_input(self) -> WebElement:
        """Get username input element"""
        pass

    @element("PASSWORD_INPUT")
    def password_input(self) -> WebElement:
        """Get password input element"""
        pass

    @element("LOGIN_BUTTON")
    def login_button(self) -> WebElement:
        """Get login button element"""
        pass

    @element("ERROR_MESSAGE")
    def error_message(self) -> WebElement:
        pass


    # Page state checks
    @log_action("Checking if login page is displayed")
    def is_page_displayed(self) -> bool:
        """Check if login page is displayed"""
        try:
            return all((
                self.login_form.is_presented(),
                self.username_input.is_presented(),
                self.password_input.is_presented(),
                self.login_button.is_presented(),
            ))
        except Exception as e:
            self._logger.error(f"Failed to check if page displayed: {e}")
            return False

    @log_action("Checking if username input is visible")
    def is_username_input_visible(self) -> bool:
        """Check if username input is visible"""
        try:
            return self.username_input.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check username visibility: {e}")
            return False

    @log_action("Checking if password input is visible")
    def is_password_input_visible(self) -> bool:
        """Check if password input is visible"""
        try:
            return self.password_input.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check password visibility: {e}")
            return False

    @log_action("Checking if login button is clickable")
    def is_login_button_clickable(self) -> bool:
        """Check if login button is clickable"""
        try:
            return self.login_button.is_clickable()
        except Exception as e:
            self._logger.error(f"Failed to check login button clickability: {e}")
            return False

    @log_action("Getting error message")
    def get_error_message(self) -> str:
        """Get error message text if displayed"""
        try:
            if self.error_message.is_visible():
                message = self.error_message.get_text()
                self._logger.warning(f"Error message: {message}")
                return message
            return None
        except Exception as e:
            self._logger.error(f"Failed to get error message: {e}")
            return None

    @log_action("Checking if error message is displayed")
    def is_error_message_displayed(self) -> bool:
        """Check if error message is displayed"""
        try:
            return self.error_message.is_visible()
        except Exception as e:
            self._logger.error(f"Failed to check error message: {e}")
            return False

    @log_action("Taking screenshot")
    def screenshot(self, file_name: str = "login_page.png") -> None:
        """Take a screenshot of the login page"""
        try:
            self.login_form.highlight_and_screenshot(file_name)
            self._logger.info(f"Screenshot saved: {file_name}")
        except Exception as e:
            self._logger.error(f"Failed to take screenshot: {e}")
