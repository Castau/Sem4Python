import Exercise_2 as utils


testoutput = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files\\utilstestout.txt'
testpath = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files'
testfilenames = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files\\utilstestfilenames.txt'
testheadlines = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week2\\Downloaded_Files\\utilstesthead.txt'

utils.filenames(testpath, testoutput)
utils.filenames_recursiv(testpath, testfilenames)
utils.firstline(testfilenames)
utils.email_lines(testfilenames)
utils.head_lines(testfilenames, testheadlines)
