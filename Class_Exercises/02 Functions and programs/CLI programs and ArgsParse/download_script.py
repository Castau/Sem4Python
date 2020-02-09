import sys
import getopt
import webget
import argparse


def run(arguments):
    for argument in args.url:
        webget.download(argument)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Arguments')
    parser.add_argument('url', nargs='+', help="URLs to download")
    args = parser.parse_args()
    print('ARGS')
    print(args)
    run(args)
    print('am main')
else:
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('url', nargs='+', help="URLs to download")
    args = parser.parse_args()
    run(args)
    print('am not main')

# BEFORE ARGSPARSE IMPLEMENTATION
# def run(arguments):

#     opts, args = getopt.getopt(arguments, 'ho:')

#     for option, optionArgument in opts:
#         print('option ' + option)
#         print('optionArgument ' + optionArgument)
#         if option == '-h':
#             print('to run: full file path -option(optional) argument argument')
#             sys.exit()
#         if option == '-o':
#             print('this option ' + option + ' reguires an optionArgument')
#             sys.exit()

#     for argument in args:
#         webget.download(argument)


# if __name__ == "__main__":
#     # run(sys.argv[1:])
#     input_lines = sys.stdin.read().split('\n')
#     run(input_lines)
#     print('am main')
# else:
#     print('am not main')
#     input_lines = sys.stdin.read().split('\n')
#     run(input_lines)
