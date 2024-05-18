from pages.main_page import MainPage


def test_wikipedia_search(driver):
    driver.get("https://www.wikipedia.org/")
    main_page = MainPage(driver)
    main_page.enter_search_query("Python (programming language)")
    main_page.click_search_button()

    # Assertions
    search_results_page = main_page.find_element(
        main_page.SEARCH_RESULTS)  # Replace with the actual locator for search results
    assert search_results_page.is_displayed()
    assert "Python (programming language)" in driver.title



