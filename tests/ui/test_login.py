from pages.login_actions import LoginPageActions


def test_login_positive(
    login_page: LoginPageActions,
    get_test_credentials: tuple[str, str],
):
    """
    Successful login with valid credentials
    """
    login_page._logger.info("Successful login with valid credentials")
    # Check if page is displayed
    assert login_page.is_page_displayed(), "Login page not displayed"

    # Check individual elements
    assert login_page.is_username_input_visible(), "Username input not visible"
    assert login_page.is_password_input_visible(), "Password input not visible"

    # Perform login
    login, password = get_test_credentials
    login_page.login(login, password)

    # Wait for redirect
    
    assert not login_page._page.login_form.is_visible(), "Login form still displayed"


def test_try_login_wo_fill_name_or_password(
    login_page: LoginPageActions,
    get_test_credentials: tuple[str, str],
):
    """
    Failed login with invalid credentials (verify error message)
    """
    login_page._logger.info("Failed login with invalid credentials (verify error message)")
    # Check if page is displayed
    assert login_page.is_page_displayed(), "Login page not displayed"

    # Check individual elements
    assert login_page.is_username_input_visible(), "Username input not visible"
    assert login_page.is_password_input_visible(), "Password input not visible"

    # Perform login
    login, password = get_test_credentials
    login_page.enter_username(login)
    assert not login_page._page.login_button.is_clickable()
    login_page.enter_username("")
    login_page.enter_password(password)
    login_page._page.login_button.click()
    error_text = login_page._page.get_error_message()
    assert error_text == "Epic sadface: Username is required", f"Another error text: {error_text}"
    login_page.enter_username(login)
    login_page.enter_password("")
    login_page._page.login_button.click()
    error_text = login_page._page.get_error_message()
    assert error_text == "Epic sadface: Password is required", f"Another error text: {error_text}"
