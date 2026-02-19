from typing import Optional, Any
from framework.logger import setup_logger

from playwright.sync_api import expect


class PlaywrightWaitManager:
    """Playwright wait implementation"""

    def __init__(self, page, timeout: int = 10000):
        self.page = page
        self.timeout = timeout
        self.logger = setup_logger(self.__class__.__name__)

    def wait_for_presence(
        self, locator: str, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element presence"""
        try:
            actual_timeout = timeout or self.timeout
            self.page.wait_for_selector(locator, timeout=actual_timeout)
            return self.page.locator(locator)
        except Exception as e:
            self.logger.warning(f"Wait for presence failed: {e}")
            return None

    def wait_for_clickable(
        self, locator: str, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element to be clickable"""
        try:
            actual_timeout = timeout or self.timeout
            locator_obj = self.page.locator(locator)
            expect(locator_obj).not_to_have_attribute(
                "disabled", None, timeout=actual_timeout
            )
            return locator_obj
        except Exception as e:
            self.logger.warning(f"Wait for clickable failed: {e}")
            return None

    def wait_for_visibility(
        self, locator: str, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element visibility"""
        try:
            actual_timeout = timeout or self.timeout
            locator_obj = self.page.locator(locator)
            locator_obj.wait_for(state="visible", timeout=actual_timeout)
            return locator_obj
        except Exception as e:
            self.logger.warning(f"Wait for visibility failed: {e}")
            return None
