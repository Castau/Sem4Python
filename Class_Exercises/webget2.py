import os
import urllib.request as req
from urllib.parse import urlparse


def download(url, to=None):
    parsed_url = urlparse(url)

    if parsed_url.scheme and parsed_url.netloc and parsed_url.path:
        # IS URL
        if (to == None):
            filename = os.path.basename(parsed_url.path)
            # Should perhaps contain a check for whether or not the file exists locally already.
            req.urlretrieve(url, filename)
        elif (to):
            req.urlretrieve(url, to)
        print("Attempting to retrieve doc from: " + url)
    else:
      # IS NOT URL
        print("Wrong url format: " + url)
