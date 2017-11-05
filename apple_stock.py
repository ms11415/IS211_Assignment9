#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 9, Part 2"""

from bs4 import BeautifulSoup
import urllib2

# opens URL
response = urllib2.urlopen("https://finance.yahoo.com/quote/AAPL/history?p=AAPL")
# reads URL data
webpage = response.read()
# creates BeautifulSoup object
soup = BeautifulSoup(webpage, "lxml")
# searches for table where player data resides
table = soup.find("table", {"data-test": "historical-prices"})

# searches for rows where player data resides
rows = table.findAll("tr")
# prints header to identify output
print "-" * 80
print "Apple Stock Historical Data"
print "Retrieved from https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
print "Close Price - Date"
print "-" * 80
# processes rows to output requested data
for row in rows:
    try:
        date = row.find("span")
        # need to find parent so that we can later find siblings
        open = date.parent
        close = open.next_sibling.next_sibling.next_sibling.next_sibling
        # condition to ignore header row
        if date.getText() != "Date":
            print close.getText(), "-", date.getText()
    # exception to ignore dividend information error
    except AttributeError:
        pass