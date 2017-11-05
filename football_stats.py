#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 9, Part 1"""

from bs4 import BeautifulSoup
import urllib2

# opens URL
response = urllib2.urlopen(
    "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns")
# reads URL data
webpage = response.read()
# creates BeautifulSoup object
soup = BeautifulSoup(webpage, "lxml")
# searches for table where player data resides
table = soup.find("table", {"class": "data"})
# searches for rows where player data resides
rows = table.findAll("tr", {"align": "right"})
# truncates list to top 20
del rows[20:]
# prints header to identify output
print "-" * 80
print "Top 20 Players from CBS NFL stats website, sorted by touchdowns"
print "Name - Position - Team - Number of Touchdowns"
print "-" * 80
# processes rows to output requested data
for row in rows:
    name = row.find("td")
    pos = name.next_sibling
    team = pos.next_sibling
    td = team.next_sibling.next_sibling.next_sibling.next_sibling
    print name.getText(), "-", pos.getText(), "-", team.getText(), "-", td.getText()