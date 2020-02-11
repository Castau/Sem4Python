# 1) Create a python file with 3 functions:
# A) def print_file_content(file) that can print content of a csv file to the console
# B) def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
# a) rewrite the function so that it gets an arbitrary number of strings instead of a list
# C) def read_csv(input_file) that take a csv file and read each row into a list
# 2) Add a functionality so that the file can be called from cli with 2 arguments
# A) path to csv file
# B) an argument - -file file_name that if given will write the content to file_name or otherwise will print it to the console.
# 3) Add a - -help cli argument to describe how the module is used

import os
import csv
import argparse

testfile = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files\\Sample-Spreadsheet-100-rows.csv'
testoutputfile = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files\\outputfile.txt'
testfileStrings = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files\\strings.txt'

parser = argparse.ArgumentParser(description='Exercise for week 2')
parser.add_argument('-path', help='path to csv file')
parser.add_argument('-output', help='output file')
parser.add_argument('-A', help='function: print_file_content')
parser.add_argument('-B', help='function: write_list_to_file')
parser.add_argument('-C', help='function: read_csv')


# A
def print_file_content(file):
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)


# B
def write_list_to_file(output_file, txtfile):
    with open(txtfile) as file_strings:
        strings = file_strings.readlines()
    print(strings)
    with open(output_file, 'w') as output:
        for string in strings:
            output.write(string)


# C
def read_csv(input_file):
    rows = []
    with open(input_file) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            rows.append(row)
    return rows


if __name__ == "__main__":
    args = parser.parse_args()
    if args.A:
        print_file_content(args.path)
    elif args.B:
        write_list_to_file(args.output, args.path)
    elif args.C:
        filecontent = read_csv(args.path)
        print(filecontent)

    # print_file_content(testfile)
    # write_list_to_file(testoutputfile, 'testStr1', 'testStr2', 'testStr3')
    # print(read_csv(testfile))
