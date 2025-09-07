import pytest
from selene import browser

@pytest.fixture(scope="function")
def set_browser_resolution():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture(scope="function")
def set_browser(set_browser_resolution):
    browser.open("https://duckduckgo.com")