from framework.locator import DriverType
from framework.logger import setup_logger, logging


class BasePage:
    """Base class for all page objects."""

    def __init__(
        self,
        driver,
        driver_type: DriverType = DriverType.PLAYWRIGHT,
        timeout: int = 10000,
    ):
        """
        Initialize LoginPage

        Args:
            driver: Selenium WebDriver or Playwright Page instance
            driver_type: Type of driver (SELENIUM or PLAYWRIGHT)
            timeout: Timeout in milliseconds for element waits
        """
        if not hasattr(driver, "locator"):
            raise TypeError(
                f"Expected Playwright Page, got {type(driver).__name__}. "
                f"Pass a Page instance for DriverType.PLAYWRIGHT"
            )
        self._driver = driver
        self._driver_type = driver_type
        self._timeout = timeout
        self._logger = setup_logger(self.__class__.__name__, logging.DEBUG)
        self._locators = None
