from .base_page import BasePage
from .locators import Locators


class SearchHelper(BasePage):

    def click_demo_button(self):
        return self.find_element(Locators.LOCATOR_MAIN_NAVBAR_DEMO_BTN, time=2).click()
