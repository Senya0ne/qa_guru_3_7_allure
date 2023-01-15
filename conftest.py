from selene.support.shared import browser
import pytest
import allure


@pytest.fixture(autouse=True)
def browser_config():
    browser.config.window_width = '1280'
    browser.config.window_height = '960'
    yield
    allure.attach(browser.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
    browser.quit()
