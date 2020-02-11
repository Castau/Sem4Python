import os
import argparse


# Create a module called utils.py and put the following functions inside:
# 1) first function takes a path to a folder and writes all filenames in the folder to a specified output file
# 2) second takes a path to a folder and write all filenames recursively(files of all sub folders to)
# 3) third takes a list of filenames and print the first line of each
# 4) fourth takes a list of filenames and print each line that contains an email(just look for @)
# 5) fifth takes a list of md files and writes all headlines(lines starting with  # ) to a file
# 6) Make sure your module can be called both from cli and imported to another module. Create a new
# module that imports utils.py and test each function.


testfile = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files\\Sample-Spreadsheet-100-rows.csv'
testfilenames = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files\\testfilenames.txt'
testoutputfile = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files\\outputfile5.txt'
testfileStrings = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files\\strings.txt'
testpath = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files'
testpath2 = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2'
testfileStrings = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files\\strings.txt'
testoutputfileheadlines = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files\\headlines.txt'

parser = argparse.ArgumentParser(description='Exercise 2 for week 2')
parser.add_argument('-folder', help='path to folder')
parser.add_argument('-input', help='input file')
parser.add_argument('-output', help='output file')
parser.add_argument('-filenames', help='function: filenames')
parser.add_argument('-recursiv', help='function: filenames_recursiv')
parser.add_argument('-firstline', help='function: firstline')
parser.add_argument('-email', help='function: firstline')


def filenames(folderpath, outputfile):
    # return os.listdir(path)
    if (os.path.isdir(folderpath)):
        with open(outputfile, 'w') as txtfile:
            txtfile.write('\n'.join(os.listdir(folderpath)))


def filenames_recursiv(folderpath, outputfile):
    with open(outputfile, 'w') as output:
        for (root, directory, files) in os.walk(folderpath):
            for filename in files:
                output.write(folderpath + '\\' + filename + '\n')


def firstline(txtfile):
    with open(txtfile) as file_names:
        filenames = file_names.readlines()
        for filename in filenames:
            with open(filename.rstrip('\n'), 'r') as file_firstline:
                print(file_firstline.readline().rstrip('\n'))


def email_lines(txtfile):
    with open(txtfile) as file_names:
        filenames = file_names.readlines()
        for filename in filenames:
            with open(filename.rstrip('\n'), 'r') as file_firstline:
                for line in file_firstline.readlines():
                    if "@" in line:
                        print(line.rstrip())


def head_lines(txtfile, outputfile):
    headlines = []
    with open(txtfile) as file_names:
        filenames = file_names.readlines()
        for filename in filenames:
            with open(filename.rstrip('\n'), 'r') as file_firstline:
                for line in file_firstline.readlines():
                    if line[0] == '#':
                        headlines.append(line)
    with open(outputfile, 'w') as output:
        output.write('\n'.join(headlines))


if __name__ == "__main__":
    args = parser.parse_args()
    if args.filenames:
        filenames(args.folder, args.output)
    elif args.recursiv:
        filenames_recursiv(args.folder, args.output)
    elif args.firstline:
        firstline(args.input)
    elif args.email:
        email_lines(args.input)
    elif args.head:
        head_lines(args.input, args.output)
    # filenames(testpath, testoutputfile)
    # filenames_recursiv(testpath, testfilenames)
    # firstline(testfilenames)
    # email_lines(testfilenames)
    # head_lines(testfilenames, testoutputfileheadlines)
