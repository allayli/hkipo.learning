#!/usr/bin/env python
    
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('ListedIPO.aspx'))

ipoListTable = soup.find_all('table', class_='newIPOTable')[0]

ipoDetails = ipoListTable.find_all('td')

#for tag in ipoDetails:
#    if len(tag.select('a')) > 0:
#        print(tag.select('a')[0].string)
#    elif len(tag.select('span')) > 0:
#        print(tag.select('span')[0].string)
#    else:
#        print(tag.string)
for tag in ipoDetails:
    for string in tag.stripped_strings:
        print(string)
