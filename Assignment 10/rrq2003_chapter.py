"""This script...
Submitted by Reyhan Quayum, rrq2003
"""

import rrq2003_paragraphs as paragraphs
import urllib.request

url = "https://www.gutenberg.org/cache/epub/996/pg996.txt"
try:
    response = urllib.request.urlopen(url)

    charactersdata = response.read().decode('utf-8')
except:
    print("Received no response from the URL!")
else:
    beginning = charactersdata.find("p007.jpg (150K)")
    ending = charactersdata.find("p007b.jpg (61K)")


