import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import os
from urllib.parse import urlparse
import requests
from requests.exceptions import HTTPError
import concurrent.futures


class NotFoundException(Exception):
    pass

def download(url, name=None):
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


