#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 9, Part 3"""

from bs4 import BeautifulSoup
import urllib2

# opens URL
response = urllib2.urlopen(
    "https://www.wunderground.com/history/airport/KNYC/2015/4/1/MonthlyHistory.html")
# reads URL data
webpage = response.read()
# creates BeautifulSoup object
soup = BeautifulSoup(webpage, "html.parser")
# searches for table where weather data resides
table = soup.find("table", {"id": "obsTable"})
# searches for rows where weater data resides
rows = table.findAll("tbody")
# delete first row of table, with no weather data
del rows[:1]
# prints header to identify output
print "-" * 80
print "Wunderground Historical Data for Central Park, April 2015"
print "Retrieved from https://www.wunderground.com/history/airport/KNYC/2015/4/1/MonthlyHistory.html"
print "Day - High Temp - Average Temp - Low Temp"
print "-" * 80
# processes rows to output requested data
for row in rows:
    day = row.find("td")
    high = row.find("span")
    average = high.findNext("span")
    low = average.findNext("span")
    print "April", day.getText(), "-", high.getText(), "-", average.getText(), "-", low.getText()