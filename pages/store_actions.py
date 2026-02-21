import time
from framework.logger import log_action
from pages.store import StorePage


class StorePageActions:
    """Actions for Store (Inventory) page"""

    def __init__(self, store_page: StorePage):
        """
        Initialize StorePageActions with a StorePage instance

        Args:
            store_page: StorePage object instance
        """
        self._page = store_page
        self._logger = store_page._logger

    # Page state checks
    @log_action("Checking if store page is displayed")
    def is_page_displayed(self) -> bool:
        """Check if store page is displayed"""
        try:
            return self._page.inventory_container.is_presented()
        except Exception as e:
            self._logger.error(f"Failed to check if store page displayed: {e}")
            return False

    # Product actions
    @log_action("Adding first product to cart")
    def add_first_product_to_cart(self) -> None:
        """Add first product in the list to cart"""
        try:
            items = self._page.inventory_items
            if not items:
                raise Exception("No inventory items found")

            first_item = items[0]
            button = first_item.find_element(*self._page._locators.ADD_TO_CART_BUTTON.to_tuple())
            button.click()
        except Exception as e:
            self._logger.error(f"Failed to add first product to cart: {e}")
            raise

    @log_action("Removing first product from cart")
    def remove_first_product_from_cart(self) -> None:
        """Remove first product from cart"""
        try:
            items = self._page.inventory_items
            if not items:
                raise Exception("No inventory items found")

            first_item = items[0]
            button = first_item.find_element(*self._page._locators.REMOVE_FROM_CART_BUTTON.to_tuple())
            button.click()
        except Exception as e:
            self._logger.error(f"Failed to remove first product from cart: {e}")
            raise

    # Cart actions
    @log_action("Opening cart page")
    def open_cart(self) -> None:
        """Click on cart icon"""
        try:
            self._page.cart_icon.click()
        except Exception as e:
            self._logger.error(f"Failed to open cart: {e}")
            raise

    @log_action("Getting cart badge value")
    def get_cart_badge_count(self) -> int:
        """Return cart badge count"""
        try:
            if not self._page.cart_badge.is_presented():
                return 0
            return int(self._page.cart_badge.text)
        except Exception as e:
            self._logger.error(f"Failed to get cart badge count: {e}")
            return 0

    # Sorting
    @log_action("Sorting products by price: low to high")
    def sort_by_price_low_to_high(self) -> None:
        """Sort products by price (low to high)"""
        try:
            self._page.sort_dropdown.click()
            time.sleep(0.5)
            self._page.sort_price_low_to_high.click()
        except Exception as e:
            self._logger.error(f"Failed to sort products by price: {e}")
            raise

    @log_action("Getting all product prices")
    def get_all_product_prices(self) -> list[float]:
        """Return list of product prices"""
        prices = []
        try:
            items = self._page.inventory_items
            for item in items:
                price_el = item.find_element(*self._page._locators.PRODUCT_PRICE.to_tuple())
                price_text = price_el.text.replace("$", "").strip()
                prices.append(float(price_text))
            return prices
        except Exception as e:
            self._logger.error(f"Failed to get product prices: {e}")
            return prices
