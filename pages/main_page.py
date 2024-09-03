from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    SEARCH_INPUT = (By.ID, "searchInput")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SEARCH_RESULTS = (By.ID, "firstHeading")  # assuming this is the locator for the first search result
    LANGUAGE_DROPDOWN = (By.ID, "searchLanguage")
    MAIN_HEADING = (By.ID, "mp-welcome")

    def enter_search_query(self, query):
        self.enter_text(self.SEARCH_INPUT, query)

    def click_search_button(self):
        self.click_element(self.SEARCH_BUTTON)

    def select_language(self, language):
        self.select_dropdown_option(self.LANGUAGE_DROPDOWN, language)

    def select_dropdown_option(self, locator, option_text):
        dropdown = self.find_element(locator)
        for option in dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text == option_text:
                option.click()
                break
