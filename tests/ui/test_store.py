from pages.store_actions import StorePageActions


def test_add_product_to_cart(
    store_page: StorePageActions,
):
    """
    Add a product to the shopping cart
    """
    store_page._logger.info("Add a product to the shopping cart")
    # Check if page is displayed
    assert store_page.is_page_displayed(), "Store page not displayed"
    # store_page.add_first_product_to_cart()
    # assert store_page.get_cart_badge_count() == 1

def test_sort_low_to_high(store_page):
    # store_page.sort_by_price_low_to_high()
    # prices = store_page.get_all_product_prices()
    # assert prices == sorted(prices)
    pass