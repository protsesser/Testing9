import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.contact_page import ContactPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def contact_page(driver):
    page = ContactPage(driver)
    file_path = "file:///" + os.path.abspath("contact_form.html")
    page.open(file_path)
    return page


def test_positive_submit(contact_page):
    contact_page.fill_name("Иван")
    contact_page.fill_email("ivan@example.com")
    contact_page.fill_message("Это корректное сообщение длиной больше 10 символов.")

    contact_page.submit()
    time.sleep(2)

    assert contact_page.is_success_displayed()


def test_negative_empty_name(contact_page):
    contact_page.fill_name("")
    contact_page.fill_email("ivan@example.com")
    contact_page.fill_message("Достаточно длинное сообщение.")

    contact_page.submit()
    time.sleep(2)

    assert contact_page.is_name_error_displayed()