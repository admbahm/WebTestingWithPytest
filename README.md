## Wikipedia Testing Framework

This project provides a Python-based automated testing framework for the Wikipedia website using Pytest and Selenium WebDriver. It adheres to the Page Object Model (POM) for better organization and maintainability.

### Features

* **Pytest:** Leverages the power and flexibility of the Pytest testing framework.
* **Selenium WebDriver:** Automates browser interactions for testing website functionality.
* **Page Object Model (POM):**  Encapsulates web page elements and actions into Python classes for easier maintenance and code reuse.

### Project Structure

```wikipedia_testing_project/
├── pages/
│   ├── base_page.py        # Base class for page objects
│   ├── main_page.py        # Page object for the Wikipedia main page
├── tests/
│   ├── test_wikipedia_search.py   # Test cases
├── conftest.py          # Pytest configuration
├── requirements.txt      # Project dependencies
└── README.md
```
### How to Run Tests

1. **Prerequisites:**
   * **Python:** Ensure you have Python 3.7 or higher installed.
   * **Virtual Environment:** Create and activate a virtual environment (recommended):
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * **Dependencies:** Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```
   * **WebDriver:** Download the appropriate WebDriver (e.g., ChromeDriver for Chrome, edgedriver for Edge) and make sure it's in your system's PATH.

2. **Run Tests:**
   * Open a terminal in the project's root directory and execute:
     ```bash
     pytest
     ```
   * This will run all the test cases located in the `tests` directory.
   * Pytest will automatically discover and execute tests based on the naming convention (files starting with `test_` or ending with `_test.py`).

### Additional Notes

* **PyCharm:** You can also run the tests directly within PyCharm using the "Run" configurations.
* **Reporting:** Pytest will generate a detailed test report in the console. You can customize this report or use plugins for additional reporting options.
* **Test Data:** If your tests require specific data, you can store it in external files (e.g., JSON or CSV) and load it during the tests.
* **Configuration:** You can further configure your tests using the `pytest.ini` file.

Running the Tests:

Now, you can run your tests directly from PyCharm:

Select Configuration: In the dropdown menu next to the green "Play" button on the toolbar, select the configuration you just created (e.g., "Run Wikipedia Tests").
Run: Click the green "Play" button (or use the keyboard shortcut).
PyCharm will execute your tests and display the results in a dedicated "Run" window. You'll see a summary of passed, failed, and skipped tests, as well as any error messages or test output. You can click on individual test names to see the details of their execution.

Additional Tips:

Run a Single Test: To run a specific test, right-click on the test file or a test function in the editor and select "Run 'pytest in <test_file_name>'".
Debugging: You can also debug your tests using PyCharm's debugger by clicking the "Bug" icon next to the "Play" button.
Test Discovery: PyCharm automatically discovers your tests. If it doesn't find any, check that your test files are named correctly (they should start with test_ or end with _test.py).