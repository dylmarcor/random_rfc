"""
Random RFC Retriever

made by Dylan Corbett - 2022

Simple command line tool for grabbing a random rfc from the web and displaying
in a few different ways. Will eventually be adpated for web usage as well.
"""

import random
import urllib.request

# Generate random number for RFC url
rand_num = random.randint(0, 9260)

# Create RFC string
rfc = 'rfc' + rand_num

