# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image
import requests
from io import BytesIO

import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


htmldata = getdata("https://www.hearthstonetopdecks.com/card-category/set/expansions/march-of-the-lich-king/")

soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])




