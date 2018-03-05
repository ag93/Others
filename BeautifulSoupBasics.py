# -*- coding: utf-8 -*-

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(source,'lxml')
# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)   


#Iterate through paragrapghs
for paragraph in soup.find_all('p'):
    #print(paragraph.string)
    print(str(paragraph.text))
    
    
#Print all text
print(soup.get_text())

#Find all links!
for url in soup.find_all('a'):
    print(url.get('href'))