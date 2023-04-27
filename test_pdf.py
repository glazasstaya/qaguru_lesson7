from pypdf import PdfReader
# TODO оформить в тест, добавить ассерты и использовать универсальный путь
reader = PdfReader("resources/docs-pytest-org-en-latest.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(page)
print(number_of_pages)
print(text)
