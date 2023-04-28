import pytest
import os
import time

from zipfile import ZipFile
from selenium import webdriver
from selene import browser
from tests.funtions import resources_path

@pytest.fixture (scope = 'function')
def browser_setting():
    download_dir = resources_path('tmp', '')
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options

#оформить в тест, добавить ассерты и использовать универсальный путь к tmp

def test_zip_download(browser_setting):

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(4)

    download_file = resources_path('tmp', 'pytest-main.zip')
    assert os.stat(download_file).st_size > 0
    with ZipFile(download_file) as pytest_main_zip:
        file_list = pytest_main_zip.namelist()
        print(file_list)
        assert 'pytest-main/' in file_list
    os.remove(download_file)