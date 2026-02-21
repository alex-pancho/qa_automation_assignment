from pages._base import BasePage
from pages.store_locators import StorePageLocators

from framework.locator import DriverType
from framework.element import element, elements, WebElement


class StorePage(BasePage):
    """Page Object Model for Store (Inventory) Page"""

    def __init__(
        self,
        driver,
        driver_type: DriverType = DriverType.PLAYWRIGHT,
        timeout: int = 10000,
    ):
        super().__init__(driver, driver_type, timeout)
        self._locators = StorePageLocators()

    # Containers
    @element("INVENTORY_CONTAINER")
    def inventory_container(self) -> WebElement:
        pass

    @element("INVENTORY_LIST")
    def inventory_list(self) -> WebElement:
        pass

    # Products
    @elements("INVENTORY_ITEM")
    def inventory_items(self) -> list[WebElement]:
        pass

    @element("PRODUCT_NAME")
    def product_name(self) -> WebElement:
        pass

    @element("PRODUCT_PRICE")
    def product_price(self) -> WebElement:
        pass

    @element("ADD_TO_CART_BUTTON")
    def add_to_cart_button(self) -> WebElement:
        pass

    @element("REMOVE_FROM_CART_BUTTON")
    def remove_from_cart_button(self) -> WebElement:
        pass

    # Header
    @element("CART_ICON")
    def cart_icon(self) -> WebElement:
        pass

    @element("CART_BADGE")
    def cart_badge(self) -> WebElement:
        pass

    @element("BURGER_MENU_BUTTON")
    def burger_menu_button(self) -> WebElement:
        pass

    @element("LOGOUT_BUTTON")
    def logout_button(self) -> WebElement:
        pass

    # Sorting
    @element("SORT_DROPDOWN")
    def sort_dropdown(self) -> WebElement:
        pass

    @element("SORT_OPTION_PRICE_LOW_TO_HIGH")
    def sort_price_low_to_high(self) -> WebElement:
        pass
