import platform
import csv
import openpyxl
import webget

url = 'https://github.com/datsoftlyngby/dat4sem2020spring-python/blob/master/iris_data.xlsx?raw=true'
webget.download(url)

# with open('Downloaded_Files/pi_30_digits.txt') as file_object:
#     contents = file_object.read()

# contents = contents.rstrip()
# print(contents)


if platform.system() == 'Windows':
    newline = ''
else:
    newline = None

with open('Downloaded_Files/iris_csv.csv', 'w', newline=newline) as csv_output_file:
    wb = openpyxl.load_workbook('Downloaded_Files/iris_data.xlsx')
    sheet = wb["Fisher's Iris Data"]
    csv_output_writer = csv.writer(csv_output_file)

    for rowOfCellObjects in sheet:
        result = []
        for cellObj in rowOfCellObjects:
            result.append(cellObj.value)

        csv_output_writer.writerow(result)
