import platform
import csv
import openpyxl
import webget
import readingFile
import os


# testing if file exists
def test_csv():
    absolutepath = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Class_Exercises\\02 Functions and programs\\Working with files\\Downloaded_Files\\iris_csv.csv'
    print((os.path.isfile(absolutepath)))
    assert (os.path.isfile(absolutepath)), 'Should be True'


# testing if header and 1st row with data is correct
def test_lines_in_csv():
    absolutepath = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Class_Exercises\\02 Functions and programs\\Working with files\\Downloaded_Files\\iris_csv.csv'
    with open(absolutepath, newline='') as csv_file:
        reader = csv.reader(csv_file)
        row1 = next(reader)
        row2 = next(reader)
        print(row1 == ['Sepal length', 'Sepal width',
                       'Petal length', 'Petal width', 'Species'])
        assert (row1 == ['Sepal length', 'Sepal width',
                         'Petal length', 'Petal width', 'Species']), 'Should be True'
        assert (row2 == ['5.1', '3.5', '1.4', '0.2',
                         'I. setosa']), 'Should be True'


if __name__ == "__main__":
    test_csv()
    test_lines_in_csv()
    print("Everything passed")
