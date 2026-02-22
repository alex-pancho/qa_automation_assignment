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
            self.first_name = first_item.inner_text().split("\n")[0]
            button = first_item.locator(
                self._page._locators.ADD_TO_CART_BUTTON.to_playwright()
            )
            button.click()

            self._logger.info(f"Added product to cart: {self.first_name}")
        except Exception as e:
            self._logger.error(f"Failed to add first product to cart: {e}")
            raise

    @log_action("Removing first product from cart")
    def remove_products_from_cart(self) -> None:
        """Remove first product from cart"""
        try:
            items = self._page.remove_from_cart_button
            if not items:
                raise Exception("No inventory items found")

            for button in items:
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
            return int(self._page.cart_badge.get_text())
        except Exception as e:
            self._logger.error(f"Failed to get cart badge count: {e}")
            return 0

    # Sorting
    @log_action("Sorting products by price: low to high")
    def sort_by_price_low_to_high(self) -> None:
        """Sort products by price (low to high)"""
        try:
            low_to_hight_value = "lohi"
            self._page.sort_dropdown.select_option(low_to_hight_value)
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
                price_text = item.inner_text().split("\n")[-2]
                price_text = price_text.replace("$", "").strip()
                prices.append(float(price_text))
            return prices
        except Exception as e:
            self._logger.error(f"Failed to get product prices: {e}")
            return prices

    @log_action("Completing checkout process")
    def complete_checkout(self, checkout_name:str, checkout_lastname:str, checkout_zip:str) -> None:
        """Complete checkout process end-to-end"""
        try:
            # click checkout
            self._page.checkout_button.click()

            # fill user info
            self._page.first_name_input.send_keys(checkout_name)
            self._page.last_name_input.send_keys(checkout_lastname)
            self._page.postal_code_input.send_keys(checkout_zip)

            # continue
            self._page.continue_button.click()

            # finish
            self._page.finish_button.click()

        except Exception as e:
            self._logger.error(f"Failed to complete checkout process: {e}")
            raise


    @log_action("Checking checkout complete page")
    def is_checkout_complete(self) -> bool:
        """Verify checkout completed successfully"""
        try:
            return self._page.checkout_complete_title.is_presented()
        except Exception as e:
            self._logger.error(f"Failed to verify checkout complete: {e}")
            return False