import os.path
import requests
from tests.funtions import resources_path


def test_downloaded_file_size():
    #сохранять и читать из tmp, использовать универсальный путь
    download_dir = resources_path('tmp', '')
    os.chdir(download_dir)
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    r = requests.get(url)
    with open('selenium_logo.png', 'wb') as file:
        file.write(r.content)
    size = os.path.getsize('selenium_logo.png')

    assert size == 30803

    download_file = resources_path('tmp', 'selenium_logo.png')
    os.remove(download_file)

