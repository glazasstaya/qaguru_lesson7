import time

from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": '/Users/kot/GitHubProjects/qa-guru/qa_guru_python_5_7_files',
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)

browser.config.driver_options = options

browser.open("https://github.com/pytest-dev/pytest")
browser.element(".d-none .Button-label").click()
browser.element('[data-open-app="link"]').click()
