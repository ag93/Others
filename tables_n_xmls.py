# -*- coding: utf-8 -*-

import bs4 as bs
import urllib.request
import pandas as pd

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

#Parsing tables!

table = soup.table

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

#Using pandas to parse tables!
    
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)
for df in dfs:
    print(df)


#Parsing XMLs!
    
source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(source,'xml')

for url in soup.find_all('loc'):
    print(url.text)