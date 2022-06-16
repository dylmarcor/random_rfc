"""
Random RFC Retriever

made by Dylan Corbett - 2022

Simple command line tool for grabbing a random rfc from the web and displaying
in a few different ways. Will eventually be adpated for web usage as well.
"""

import sys
import random
import urllib.request

# Generate random number for RFC url
rand_num = random.randint(0, 9260)

# Create initial RFC url
rfc = "https://www.rfc-editor.org/rfc/rfc" + str(rand_num)

# Command intro - grab type of file wanted (default:txt)
# print("What file would you like the random RFC in?")
# print("Default is txt")
# file_type = input()
file_type = 'txt'

def rfc_generator(rfc, f_format):

    if (f_format):
        return rfc  + '.' + f_format
    else:
        return rfc + '.txt'

# From RFC Generator request URL and get results
rfc_url = urllib.request.urlopen(rfc_generator(rfc, file_type))

for line in rfc_url:
    line = line.decode("utf-8")
    print(line.rstrip('\n'))
