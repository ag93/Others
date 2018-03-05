# -*- coding: utf-8 -*-
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

#grab the links from just the nav bar:
nav = soup.nav
for url in nav.find_all('a'):
    print(url.get('href'))

#Print paragraphs from body
body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)
    
"""sometimes there might be multiple tags with the same names, but different classes, 
and you might want to grab information from a specific tag with a specific class.
For example, our page that we're working with has a div tag with the class of "body".
We can work with this data like so:""" 
   
for div in soup.find_all('div', class_='body'):
    print(div.text)
    
# class_='body', which allows us to work with a specific class of tag.