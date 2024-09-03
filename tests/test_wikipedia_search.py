from pages.main_page import MainPage

class TestWikipedia:
    def test_wikipedia_search(self, driver):
        # Arrange
        driver.get("https://www.wikipedia.org/")
        main_page = MainPage(driver)

        # Act
        main_page.enter_search_query("Python (programming language)")
        main_page.click_search_button()

        # Assert
        search_results_page = main_page.find_element(
            main_page.SEARCH_RESULTS)  # Replace with the actual locator for search results
        assert search_results_page.is_displayed()
        assert "Python (programming language)" in driver.title

    def test_wikipedia_language_selection(self, driver):
        # Arrange
        driver.get("https://www.wikipedia.org/")
        main_page = MainPage(driver)

        # Act
        main_page.select_language("Español")

        # Assert
        assert "Wikipedia" in driver.title
        assert driver.current_url == "https://es.wikipedia.org/wiki/Wikipedia:Portada"
        assert main_page.get_text(main_page.MAIN_HEADING) == "Bienvenidos a Wikipedia,"
