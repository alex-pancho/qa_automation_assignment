from urllib.parse import urlparse


def logout(_url, page):
    """Make logout"""
    url = _url
    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    logout_url = f"{base_url}/logout"
    page._page._driver.goto(logout_url)
    page._page._driver.goto(url)
