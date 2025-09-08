from selene import browser, be, have, by

def test_failed_search (set_browser):
    browser.config.timeout = 8
    browser.element('[id="searchbox_input"]').should(be.blank).type('Xx9abT72kLmQ').press_enter()
    browser.element(by.partial_text('ничего не найдено')).should(be.visible)
    #browser.element('html').should(have.text('ничего не найдено'))