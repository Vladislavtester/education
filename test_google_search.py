import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(800,600)
    yield driver
    driver.quit()

def test_open_site(browser):
    browser.get ("https://google.com")
    element = browser.find_element(By.NAME, "q")
    element.send_keys("коты в рубашках"+Keys.ENTER)
    assert "коты" in browser.title





