from abc import ABC, abstractmethod
from typing import List


class BaseScreenshotManager(ABC):
    """Abstract screenshot manager interface"""

    @abstractmethod
    def highlight_and_screenshot(self, element, file_name: str = "element.png"):
        pass

    @abstractmethod
    def highlight_and_screenshot_many(
        self, elements: List, file_name: str = "elements.png"
    ):
        pass

class PlaywrightScreenshotManager(BaseScreenshotManager):
    """Playwright screenshot implementation"""

    def __init__(self, page):
        self.page = page

    def highlight_and_screenshot(self, locator, file_name: str = "element.png"):
        """Highlight element with red border and take screenshot"""
        self.page.evaluate("elem => elem.scrollIntoView()", locator.element_handle())
        self.page.evaluate(
            "elem => elem.style.border='3px solid red'", locator.element_handle()
        )
        self.page.screenshot(path=file_name)

    def highlight_and_screenshot_many(
        self, locators: List, file_name: str = "elements.png"
    ):
        """Highlight multiple elements and take screenshot"""
        for locator in locators:
            self.page.evaluate(
                "elem => elem.scrollIntoView()", locator.element_handle()
            )
            self.page.evaluate(
                "elem => elem.style.border='3px solid red'", locator.element_handle()
            )
        self.page.screenshot(path=file_name)
