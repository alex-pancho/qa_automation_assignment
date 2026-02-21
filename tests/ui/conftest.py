import os
import pytest
from contextlib import contextmanager
from dotenv import load_dotenv

from framework.driver_factory import DriverFactory
from framework.locator import DriverType
from framework.logger import log_info

from pages.login import LoginPage
from pages.login_actions import LoginPageActions
from pages.store import StorePage
from pages.store_actions import StorePageActions


load_dotenv()


DEBUG_URL = os.getenv("DEBUG_URL", "https://127.0.0.1")
BASE_UI_URL = os.getenv("BASE_UI_URL", "https://www.example.com")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
BROWSER = os.getenv("BROWSER", "chromium").lower()


@pytest.fixture(scope="session")
def get_test_credentials() -> tuple[str, str]:
    """Fixture to provide test credentials from environment variables"""
    test_username = os.getenv("TEST_USERNAME", "testname")
    test_password = os.getenv("TEST_PASSWORD", "password")
    return test_username, test_password


@contextmanager
def build_context(url: str):
    """Context manager to create and cleanup browser context"""
    context, browser, playwright = DriverFactory.create_playwright_local(
        browser_type=BROWSER, headless=HEADLESS
    )
    page = context.new_page()

    try:
        page.goto(url)
        yield page
    finally:
        context.close()
        browser.close()
        playwright.stop()


@pytest.fixture(scope="module")
def base_page():
    """Base fixture that provides page object and URL"""
    url = DEBUG_URL if DEBUG else BASE_UI_URL
    with build_context(url) as page:
        yield url, page


@pytest.fixture()
def login_page(base_page):
    """fixture for login page"""
    url, page = base_page
    log_info(f"GET URL: {url}")
    login_page = LoginPage(page, DriverType.PLAYWRIGHT)
    login_page_actions = LoginPageActions(login_page)
    yield login_page_actions
    login_page_actions._logout()


@pytest.fixture()
def store_page(base_page, get_test_credentials):
    """fixture for login page"""
    url, page = base_page
    log_info(f"GET URL: {url}")
    login_page = LoginPage(page, DriverType.PLAYWRIGHT)
    login_page_actions = LoginPageActions(login_page)
    login, password = get_test_credentials
    login_page_actions.login(login, password)
    store_page = StorePage(page, DriverType.PLAYWRIGHT)
    store_page_actions = StorePageActions(store_page)
    yield store_page_actions
    login_page_actions._logout()
