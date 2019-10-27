#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Written By:
#       S.S.B
#       surajsinghbisht054@gmail.com
#       bitforestinfo.blogspot.com
#   
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
# Import Modules
import urllib.request, urllib.error, urllib.parse
import re

# Downloading Live Score XML Code From Website and reading also
xml_data = urllib.request.urlopen('http://static.cricinfo.com/rss/livescores.xml').read()

# Pattern For Searching Score and link
pattern = "<item>(.*?)</item>"

# Finding Matches
for i in re.findall(pattern, xml_data, re.DOTALL):
    result = re.split('<.+?>',i)
    print((result[1], result[3])) # Print Score