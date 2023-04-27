import os.path

import requests

def test_downloaded_file_size():
    # TODO сохранять и читать из tmp, использовать универсальный путь
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    r = requests.get(url)
    with open('selenium_logo.png', 'wb') as file:
        file.write(r.content)

    size = os.path.getsize('selenium_logo.png')

    assert size == 30803

