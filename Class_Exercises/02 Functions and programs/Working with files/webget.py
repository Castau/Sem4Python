import os
import urllib.request as req
from urllib.parse import urlparse


def download(url, to=None):
    parsed_url = urlparse(url)
    fullfilename = "Downloaded_Files/" + os.path.basename(parsed_url.path)
    absolutepath = os.path.join(os.path.dirname(__file__), fullfilename)
    fileexists = os.path.isfile(absolutepath)

    if parsed_url.scheme and parsed_url.netloc and parsed_url.path:
        if fileexists:
            print("File already exits here: " +
                  fullfilename + ", download aborted")
            return fullfilename

        if (to == None):
            req.urlretrieve(url, absolutepath)
            print("Downloading file to: " + absolutepath)

        elif to and os.path.isfile(to):
            req.urlretrieve(url, to)
            print("Downloading file to: " + to)
    else:
        print("Error in URL format: " + url)
