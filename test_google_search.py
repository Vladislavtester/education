import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

@pytest.fixture(scope="function")
def browser():
    options = Options()
#    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(800,600)
    stealth(driver,
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.105 Safari/537.36',
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    yield driver
    driver.quit()

def test_open_site(browser):
    browser.get ("https://duckduckgo.com/")
    element = browser.find_element(By.NAME, "q")
    element.send_keys("коты в рубашках"+Keys.ENTER)
    assert "коты в рубашках" in browser.title




