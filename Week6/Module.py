# Create a module containing a class with the following methods:
# 1) init(self, url_list)
# 2) download(url, filename) raises NotFoundException when url returns 404
# 3) multi_download(url_list) uses threads to download multiple urls as text and stores filenames as a property
# 4) iter() returns an iterator
# 5) next() returns the next filename(and stops when there are no more)
# 6) urllist_generator() returns a generator to loop through the urls
# 7) avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
# 8) hardest_read() returns the filename of the text with the highest vowel score(use all the cpu cores on the computer for this work).

import os
from urllib.parse import urlparse
import requests
from requests.exceptions import HTTPError
import concurrent.futures
import re
import multiprocessing
import concurrent.futures.process
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Queue

class NotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)

last = None

class moduleClass():
    def __init__(self, url_list):
        self.urlList = url_list
        self.count = 0
        

    def __iter__(self):
        self.count = 0
        return self


    def __next__(self): 
        self.count += 1
        if self.count < len(self.url_list):
            return os.path.basename(urlparse(self.urlList[self.count]).path)
        else:
            raise StopIteration


    def urllist_generator(self):
        for url in self.urlList:
            yield url


    def download(self, url, name=None):
        filename = os.path.basename(urlparse(url).path)
        if(name):
            filename = name
        fullfilename = 'Downloaded_Files/' + filename
        fileexists = os.path.isfile(fullfilename)

        if fileexists:
            print(f'File already exits here: {fullfilename}, download aborted')
            return fullfilename
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()

            with open(fullfilename, 'wb') as output:
                output.write(response.content)
            print(f'Downloading file to: {fullfilename}')

        except HTTPError as httpError:
            if response.status_code == 404:
                raise NotFoundException(f'Content not found: {httpError}')
            else:
                raise Exception(f'An error occured: {httpError}')
    

    # Example used: https://docs.python.org/3/library/concurrent.futures.html
    def multi_download(self, url_list):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(url_list)) as executor:
            future_to_url = {executor.submit(self.download, url): url for url in url_list}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    future.result()
                except Exception as e:
                    print(f'An error occured:{url, e}')

    def avg_vowels(self, contentlist: str):
        content = (''.join(contentlist))
        wordcount = len(content.split(' '))
        vowelcount = len(re.findall(r'[aeiou]', content, flags=re.I))
        return vowelcount/wordcount

    # I GIVE UP
    # def hardest_read(self, filepath):
    #     global last 
    #     last = {'':0}
    #     queue = Queue()
    #     textfiles = []
    #     for item in self.urlList:
    #         textfiles.append(filepath + os.path.basename(urlparse(item).path))

    #     with ProcessPoolExecutor(multiprocessing.cpu_count()) as executor:
    #         for text in textfiles:
    #             with open(text, encoding='utf8') as textfile:
    #                 vowelCount = self.avg_vowels(textfile.readlines())
    #                 queue.put({text:vowelCount})
        
    #     print('before while')
    #     while (queue):
    #         current = queue.heappop
    #         print('AM HERE')
    #         print(current)
    #         if(current.value() > last):
    #             last = current
    #     return last[0]






        
    
