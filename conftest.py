import pytest
from selene import browser

@pytest.fixture()
def set_browser(scope="function"):
    browser.open("https://duckduckgo.com")