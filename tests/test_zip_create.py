import pytest
from zipfile import ZipFile
import os
from tests.funtions import resources_path

dir_to_zip = resources_path('resources', '')
print(dir_to_zip)
for files in os.walk(dir_to_zip):
    print(files)

def test_zip_file_create():
    zip_file = resources_path('resources', 'newfile.zip')
    dir_to_zip = resources_path('resources', '')
    content = os.listdir(dir_to_zip)

    with ZipFile(zip_file, mode = 'w') as newzip:
        os.chdir(dir_to_zip)
        for f in content:
            if f != 'newfile.zip':
                newzip.write(f)

    with ZipFile(zip_file)  as newzip:
        content_list = newzip.namelist()
        print(content_list)
        for f in content:
            if f != 'newfile.zip':
                assert f in content_list
        assert len(content) == len(content_list)

    os.remove(zip_file)


