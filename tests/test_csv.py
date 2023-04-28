import csv
import pytest
from tests.funtions import resources_path

# оформить в тест, добавить ассерты и использовать универсальный путь

def test_csv_write_and_read():
    file = resources_path('resources', 'eggs.csv')
    rows = []

    with open(file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(file) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
            print(row)

    assert rows[0] == ['Anna', 'Pavel', 'Peter']

