import pytest
from selenium import webdriver
from TestFramework.settings import driver_path


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path=driver_path)
    yield driver
    driver.quit()
