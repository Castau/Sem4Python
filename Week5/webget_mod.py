import os
import urllib.request as req
from urllib.parse import urlparse


def download(url, name=None, to=None):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if(name):
        filename = name
    fullfilename = "Downloaded_Files/" + filename
    fileexists = os.path.isfile(fullfilename)

    if parsed_url.scheme and parsed_url.netloc and parsed_url.path:
        if fileexists:
            print("File already exits here: " +
                  fullfilename + ", download aborted")
            return fullfilename

        if (to == None):
            req.urlretrieve(url, fullfilename)
            print("Downloading file to: " + fullfilename)

        elif to and os.path.isfile(to):
            req.urlretrieve(url, to)
            print("Downloading file to: " + to + filename)
    else:
        print("Error in URL format: " + url)
