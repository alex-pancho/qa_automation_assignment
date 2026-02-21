from typing import Optional, List, Any
from framework.logger import log_action, setup_logger, log_waning
from framework.locator import Locator, DriverType

try:
    from framework.waiter import PlaywrightWaitManager
    from framework.screenshot import PlaywrightScreenshotManager
    from framework.actions import PlaywrightElementActions
except ImportError:
    log_waning("Playwright not installed, PlaywrightWebElement will not work")


class WebElement:
    """Type-safe WebElement abstraction supporting both Selenium and Playwright"""

    def __init__(
        self,
        locator: Locator,
        driver: Any,
        driver_type: DriverType = DriverType.SELENIUM,
        timeout: int = 10000,
    ):
        self._locator = locator
        self._driver = driver
        self._driver_type = driver_type
        self._timeout = timeout
        self._logger = setup_logger(self.__class__.__name__)

        self._initialize_managers()

    def _initialize_managers(self):
        """Initialize appropriate managers based on driver type"""
        self._wait_manager = PlaywrightWaitManager(self._driver, self._timeout)
        self._screenshot_manager = PlaywrightScreenshotManager(self._driver)

    @log_action("Finding element")
    def find(self) -> Optional[Any]:
        """Find element"""
        playwright_locator = self._locator.to_playwright()
        return self._wait_manager.wait_for_presence(
            playwright_locator, self._timeout
        )

    @log_action("Checking if clickable")
    def is_clickable(self) -> bool:
        """Check if element is clickable"""
        playwright_locator = self._locator.to_playwright()
        element = self._wait_manager.wait_for_clickable(
            playwright_locator, timeout=100
        )
        return element is not None

    @log_action("Checking if visible")
    def is_visible(self, timeout: int = 500) -> bool:
        """Check if element is visible"""
        old_timeout = self._timeout
        self._timeout = timeout
        element = self.find()
        self._timeout = old_timeout
        if element is None:
            return False

        return element.is_visible()

    @log_action("Checking if presented")
    def is_presented(self) -> bool:
        """Check if element is present on page"""
        return self.find() is not None

    @log_action("Performing click")
    def click(self, x_offset: int = 0, y_offset: int = 0):
        """Click element"""
        element = self.find()

        if not element:
            raise ElementNotFound(f"Element {self._locator} not found")

        actions = PlaywrightElementActions(self._driver, element)

        actions.click(x_offset, y_offset)

    @log_action("Sending keys")
    def send_keys(self, text: str):
        """Type text into element"""
        element = self.find()

        if not element:
            raise ElementNotFound(f"Element {self._locator} not found")

        actions = PlaywrightElementActions(self._driver, element)

        actions.send_keys(text)

    @log_action("Getting text")
    def get_text(self) -> str:
        """Get element text"""
        element = self.find()

        if not element:
            return ""

        actions = PlaywrightElementActions(self._driver, element)

        return actions.get_text()

    @log_action("Getting attribute")
    def get_attribute(self, attr_name: str) -> Optional[str]:
        """Get element attribute"""
        element = self.find()

        if not element:
            return None

        actions = PlaywrightElementActions(self._driver, element)

        return actions.get_attribute(attr_name)

    @log_action("Taking screenshot")
    def highlight_and_screenshot(self, file_name: str = "element.png"):
        """Highlight element with red border and take screenshot"""
        element = self.find()
        if element:
            self._screenshot_manager.highlight_and_screenshot(element, file_name)


class element:
    def __init__(self, locator_name: str):
        self.locator_name = locator_name

    def __call__(self, func) -> WebElement:
        def wrapper(obj):
            locator = getattr(obj._locators, self.locator_name)
            return WebElement(
                locator,
                obj._driver,
                obj._driver_type,
                obj._timeout,
            )

        return property(wrapper)


class ManyWebElements(WebElement):
    """Collection of elements"""

    @log_action("Finding elements")
    def find(self) -> List[Any]:
        """Find multiple elements"""
        playwright_locator = self._locator.to_playwright()
        try:
            return self._driver.locator(playwright_locator).all()
        except Exception as e:
            self._logger.warning(f"Find many failed: {e}")
            return []

    @log_action("Counting elements")
    def count(self) -> int:
        """Get count of elements"""
        elements = self.find()
        return len(elements)

    @log_action("Getting all text")
    def get_all_text(self) -> List[str]:
        """Get text from all elements"""
        elements = self.find()

        return [elem.text_content() or "" for elem in elements]

    def __getitem__(self, index: int):
        """Access element by index"""
        elements = self.find()
        return elements[index]

class elements:
    def __init__(self, locator_name: str):
        self.locator_name = locator_name

    def __call__(self, func) -> WebElement:
        def wrapper(obj):
            locator = getattr(obj._locators, self.locator_name)
            return ManyWebElements(
                locator,
                obj._driver,
                obj._driver_type,
                obj._timeout,
            )

        return property(wrapper)

class ElementNotFound(Exception):
    """Custom exception for element not found"""
    pass
