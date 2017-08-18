#!/usr/bin/env python
# pylint: disable=C0103

import urllib.request
import csv

from bs4 import BeautifulSoup

AASTOCK_URL = 'http://www.aastocks.com/tc/IPO/ListedIPO.aspx?iid=ALL&orderby=DA&value=DESC&index='
MAX_PAGE = 15

def getAAStockIpoPage(page):
    """Get HTML Page From aa stock"""
    url = AASTOCK_URL + str(page)
    with urllib.request.urlopen(url) as response:
        html = response.read()
        return html


def parseAAStockIpoPage(page):
    """Parse Page and return list that contains an IPO entry"""

    soup = BeautifulSoup(page, 'html5lib')

    ipoListTable = soup.find_all('table', class_='newIPOTable')[0]

    ipoDetails = ipoListTable.find_all('tr', {"class": ["DR", "ADR"]})

    details = []
    for tag in ipoDetails:
        row = []
        for string in tag.stripped_strings:
            row.append(string)
        details.append(row)
    return details


with open('test.csv', 'w', newline='') as csvfile:
    dataWriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for x in range(1, MAX_PAGE):
        pageDetails = parseAAStockIpoPage(getAAStockIpoPage(x))
        dataWriter.writerows(pageDetails)
