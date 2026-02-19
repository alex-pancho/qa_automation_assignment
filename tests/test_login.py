from pages.login_actions import LoginPageActions


def test_login_positive(
    login_page: LoginPageActions,
    get_test_credentials: tuple[str, str],
):
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
    assert not login_page._page.login_button.is_clickable()


# def test_signup_redirect(
#     login_page: LoginPageActions,
# ):
#     # Check if login page is displayed
#     assert login_page.is_page_displayed(), "Login page not displayed"

#     login_page.click_sign_up()
#     # Check if sign up page is displayed
#     assert not login_page._page.sign_up_link.is_visible(), "Login page still displayed"
