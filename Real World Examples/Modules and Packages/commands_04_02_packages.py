""" The Hierarchy of Packages """

import urllib.request

# retrieve google.com home page
print(urllib.request.urlopen('http://www.google.com'))

# get the path to urllib package
print(urllib.__path__)
