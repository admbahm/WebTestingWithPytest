from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    SEARCH_INPUT = (By.ID, "searchInput")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SEARCH_RESULTS = (By.ID, "firstHeading")  # assuming this is the locator for the first search result

    def enter_search_query(self, query):
        self.enter_text(self.SEARCH_INPUT, query)

    def click_search_button(self):
        self.click_element(self.SEARCH_BUTTON)
