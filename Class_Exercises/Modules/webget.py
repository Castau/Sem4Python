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


# import os
# import requests as req
# from urllib.parse import urlparse


# def download(url, to=None):
#     parsed_python_url = urlparse(url)

#     local_data = os.path.isfile(
#         "./" + os.path.basename(parsed_python_url.path))
#     if local_data:
#         print("File already exists1")
#         return os.path.basename(parsed_python_url.path)
#     if to and os.path.isfile(to):
#         print("File already exists2")
#         return to
#     else:
#         data = req.get(url)
#         location = "./" + os.path.basename(parsed_python_url.path)
#         if to:
#             location = to
#         open(location, "wb").write(data.content)
#         print("saving file")
#         return location
