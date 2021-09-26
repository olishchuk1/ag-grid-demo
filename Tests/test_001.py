from TestFramework.page_object import SearchHelper


def test_001(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.click_demo_button()
