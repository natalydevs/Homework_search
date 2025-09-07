from selene import browser, be, have

def test_successful_search (set_browser):
    browser.config.timeout = 8
    browser.element('[id="searchbox_input"]').should(be.blank).type('site:qa.guru').press_enter()
    browser.element('a[href="https://qa.guru/"]').should(be.visible).click()
    browser.should(have.title_containing('QA.GURU'))