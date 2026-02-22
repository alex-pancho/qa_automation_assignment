from dataclasses import dataclass
from framework.locator import Locator, LocatorType


@dataclass
class StorePageLocators:
    """All locators for the Store (Inventory) page"""

    # Main containers
    INVENTORY_CONTAINER = Locator(
        type=LocatorType.XPATH,
        value='//div[@id="inventory_container"]',
    )

    INVENTORY_LIST = Locator(
        type=LocatorType.XPATH,
        value='//div[@class="inventory_list"]',
    )

    # Products
    INVENTORY_ITEM = Locator(
        type=LocatorType.XPATH,
        value='//div[@class="inventory_item"]',
    )

    PRODUCT_NAME = Locator(
        type=LocatorType.XPATH,
        value='.//div[@class="inventory_item_name"]',
    )

    PRODUCT_PRICE = Locator(
        type=LocatorType.XPATH,
        value='.//div[@class="inventory_item_price"]',
    )

    ADD_TO_CART_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='.//button[contains(@id,"add-to-cart")]',
    )

    REMOVE_FROM_CART_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='.//button[contains(@id,"remove")]',
    )

    # Header / navigation
    CART_ICON = Locator(
        type=LocatorType.XPATH,
        value='//a[@class="shopping_cart_link"]',
    )

    CART_BADGE = Locator(
        type=LocatorType.XPATH,
        value='//span[@class="shopping_cart_badge"]',
    )

    BURGER_MENU_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//button[@id="react-burger-menu-btn"]',
    )

    LOGOUT_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//a[@id="logout_sidebar_link"]',
    )

    # Sorting
    SORT_DROPDOWN = Locator(
        type=LocatorType.XPATH,
        value='//select[@class="product_sort_container"]',
    )

    SORT_OPTION_PRICE_LOW_TO_HIGH = Locator(
        type=LocatorType.XPATH,
        value='//option[@value="lohi"]',
    )

    # Cart page
    CHECKOUT_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//button[@id="checkout"]',
    )

    CONTINUE_SHOPPING_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//button[@id="continue-shopping"]',
    )

    CART_ITEM = Locator(
        type=LocatorType.XPATH,
        value='//div[@class="cart_item"]',
    )

    # Checkout: Your Information
    FIRST_NAME_INPUT = Locator(
        type=LocatorType.XPATH,
        value='//input[@id="first-name"]',
    )

    LAST_NAME_INPUT = Locator(
        type=LocatorType.XPATH,
        value='//input[@id="last-name"]',
    )

    POSTAL_CODE_INPUT = Locator(
        type=LocatorType.XPATH,
        value='//input[@id="postal-code"]',
    )

    CONTINUE_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//input[@id="continue"]',
    )

    # Checkout: Overview
    FINISH_BUTTON = Locator(
        type=LocatorType.XPATH,
        value='//button[@id="finish"]',
    )

    # Checkout: Complete
    CHECKOUT_COMPLETE_TITLE = Locator(
        type=LocatorType.XPATH,
        value='//h2[@class="complete-header" and text()="Thank you for your order!"]',
    )

    CHECKOUT_COMPLETE_CONTAINER = Locator(
        type=LocatorType.XPATH,
        value='//*[@id="checkout_complete_container"]',
    )

    BACK_TO_SHOP = Locator(
        type=LocatorType.XPATH,
        value='//*[@id="back-to-products"]',
    )