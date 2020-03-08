import Module
import os
from urllib.parse import urlparse
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from collections import OrderedDict

url_csv200 = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=F&Tid=2008K1%2C2009K1%2C2010K1%2C2011K1%2C2012K1%2C2013K1%2C2014K1%2C2015K1%2C2016K1%2C2017K1%2C2018K1%2C2019K1%2C2020K1'
url_404 = 'http://httpstat.us/404'
url_403 = 'http://httpstat.us/403'

URLS = [
    'http://www.gutenberg.org/cache/epub/16328/pg16328.txt',
    'https://www.gutenberg.org/files/84/84-0.txt',
    'http://www.gutenberg.org/cache/epub/25525/pg25525.txt',
    'https://www.gutenberg.org/files/74/74-0.txt',
    'https://www.gutenberg.org/files/43/43-0.txt',
    'https://www.gutenberg.org/files/1661/1661-0.txt',
    'http://www.gutenberg.org/cache/epub/174/pg174.txt',
    'http://www.gutenberg.org/cache/epub/345/pg345.txt',
    'https://www.gutenberg.org/files/1342/1342-0.txt',
    'http://www.gutenberg.org/cache/epub/376/pg376.txt'
]

filepath = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week6\\Downloaded_Files\\'
testModule = Module.moduleClass(URLS)

def getAvgVowelCountPerFile(urls):
    files = {}
    for url in urls:
        filename = os.path.basename(urlparse(url).path)
        fullfilename = filepath + filename
        vowelCount = 0
        with open(fullfilename, encoding='utf8') as textfile:
            vowelCount = testModule.avg_vowels(textfile.readlines())
            files[filename] = vowelCount
    return files


def sortBooks(data):
    books_sorted = OrderedDict(
        sorted(data.items(), key=lambda x: x[1]))
    return books_sorted

def barplotBooks(data):
    plt.figure()
    plt.bar(data.keys(), data.values(),
            width=0.7, align='center', zorder=3, color='rebeccapurple')
    title = 'Books sorted per avg vowel per word'
    plt.title(title, fontsize=15)
    plt.xlabel('Books', fontsize=12)
    plt.ylabel('Average vowels per word', fontsize=12)
    plt.grid(axis='y', linestyle='dotted', zorder=0)
    plt.xticks(rotation=45, ha='right')
    plt.show()

if __name__ == '__main__':
    # iter
    print(testModule.__iter__())
    # next
    print(testModule.__next__())
    print(testModule.__next__())
    # urllist_generator
    print(testModule.urllist_generator())
    # download
    testModule.download(URLS[0])
    # multi_download
    testModule.multi_download(URLS)
    # avg_vowels
    with open(filepath + testModule.__next__(), encoding='utf8') as textfile:
        vowelCount = testModule.avg_vowels(textfile.readlines())
        print(vowelCount)
    # hardest_read ---> Does not work yet
    # print(testModule.hardest_read())
    # getAvgVowelCountPerFile(URLS)
    barplotBooks(sortBooks(getAvgVowelCountPerFile(URLS)))
