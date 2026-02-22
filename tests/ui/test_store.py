from pages.store_actions import StorePageActions


def test_add_product_to_cart(
    store_page: StorePageActions,
):
    """
    3	Add a product to the shopping cart
    4	Remove a product from the shopping cart
    """
    store_page._logger.info("Add a product to the shopping cart")
    # Check if page is displayed
    assert store_page.is_page_displayed(), "Store page not displayed"
    store_page.add_first_product_to_cart()
    assert store_page.get_cart_badge_count() == 1
    store_page.remove_products_from_cart()
    assert store_page.get_cart_badge_count() == 0, "Not all products was remove"


def test_complete_checkout(
    store_page: StorePageActions,
    
):
    """
    5 Complete checkout process (end-to-end)
    """
    # Check store page
    assert store_page.is_page_displayed(), "Store page not displayed"
    # Add product to cart
    store_page.add_first_product_to_cart()
    assert store_page.get_cart_badge_count() == 1, "Product not added to cart"
    # Open cart
    store_page.open_cart()
    # Start checkout
    checkout_name = "User"
    checkout_lastname = "Lastname"
    checkout_zip = "123456"
    store_page.complete_checkout(checkout_name, checkout_lastname, checkout_zip)
    assert store_page.is_checkout_complete(), "CRITICAL: Checkout was not completed successfully"


def test_sort_low_to_high(
    store_page: StorePageActions,
):
    """
    6	Verify product sorting functionality (e.g., price low-to-high)	Optional
    """
    store_page.sort_by_price_low_to_high()
    prices = store_page.get_all_product_prices()
    assert prices == sorted(prices)
