import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


@pytest.fixture(scope="module")
def driver():
    service = Service(executable_path="/usr/local/bin/msedgedriver")  # Path to your msedgedriver executable
    driver = webdriver.Edge(service=service)  # Use service instead of executable_path
    yield driver
    driver.quit()
