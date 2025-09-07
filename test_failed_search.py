from selene import browser, be, have

def test_failed_search (set_browser):
    browser.config.timeout = 8
    browser.element('[id="searchbox_input"]').should(be.blank).type('Xx9abT72kLmQ').press_enter()
    browser.all('h2 a').should(have.size(0))
    print("Нет результатов поиска")