from abc import ABC, abstractmethod
from typing import Optional
from framework.logger import log_action, log_waning


class BaseElementActions(ABC):
    """Abstract element actions interface"""

    @abstractmethod
    def click(self, x_offset: int = 0, y_offset: int = 0, hold_seconds: float = 0):
        pass

    @abstractmethod
    def right_click(self, x_offset: int = 0, y_offset: int = 0):
        pass

    @abstractmethod
    def send_keys(self, text: str, clear_first: bool = True):
        pass

    @abstractmethod
    def get_text(self) -> str:
        pass

    @abstractmethod
    def get_attribute(self, attr_name: str) -> Optional[str]:
        pass

    @abstractmethod
    def select_by_text(self, text: str):
        pass


class PlaywrightElementActions(BaseElementActions):
    """Playwright element actions implementation"""

    def __init__(self, page, locator):
        self.page = page
        self.locator = locator

    @log_action("Clicking element")
    def click(self, x_offset: int = 0, y_offset: int = 0, hold_seconds: float = 0):
        """Click element with offset and hold duration"""
        kwargs = {}
        if x_offset or y_offset:
            kwargs["position"] = {"x": x_offset, "y": y_offset}
        if hold_seconds:
            kwargs["delay"] = int(hold_seconds * 1000)

        self.locator.click(**kwargs)

    @log_action("Right-clicking element")
    def right_click(self, x_offset: int = 0, y_offset: int = 0):
        """Right-click element"""
        kwargs = {"button": "right"}
        if x_offset or y_offset:
            kwargs["position"] = {"x": x_offset, "y": y_offset}

        self.locator.click(**kwargs)

    @log_action("Sending keys")
    def send_keys(self, text: str, clear_first: bool = True):
        """Type text into element"""
        if clear_first:
            self.locator.clear()
        self.locator.fill(text)

    @log_action("Getting text")
    def get_text(self) -> str:
        """Get element text"""
        return self.locator.text_content() or ""

    @log_action("Getting attribute")
    def get_attribute(self, attr_name: str) -> Optional[str]:
        """Get element attribute"""
        return self.locator.get_attribute(attr_name)

    @log_action("Selecting by text")
    def select_by_text(self, text: str):
        """Select option from dropdown by visible text"""
        self.locator.select_option(text)
