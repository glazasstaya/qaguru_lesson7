from zipfile import ZipFile

zip_file = ZipFile('resources/hello.zip')
print(zip_file.namelist())
text = zip_file.read('Hello.txt')
print(text)
zip_file.close()

with ZipFile('resources/hello.zip') as hello_zip:
    hello_zip.extract('Hello.txt')