from selenium.webdriver.common.by import By


class Locators:
    LOCATOR_MAIN_NAVBAR_DEMO_BTN = (By.LINK_TEXT, "Demo")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
