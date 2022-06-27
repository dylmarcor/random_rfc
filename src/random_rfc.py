"""
Random RFC Retriever

made by Dylan Corbett - 2022

Simple command line tool for grabbing a random rfc from the web and displaying
in a few different ways. Will eventually be adpated for web usage as well.
"""

import sys
import random
import subprocess
import urllib.request

# Generate random number for RFC url
rand_num = random.randint(0, 9260)

# Create initial RFC url
rfc = "https://www.rfc-editor.org/rfc/rfc" + str(rand_num) + '.txt'
rfc_url = urllib.request.urlopen(rfc)

# Display RFC
for line in rfc_url:
    print(line.decode("utf-8").rstrip())

# TODO: Add specific RFC if desired function
# TODO: Figure out how to pipe print to less shell command
# Process output to 'less' command in shell
# subprocess.run(['less'], stdout=subprocess.PIPE, input=rfc_url.read().decode('utf-8'), shell= True, text=True).stdout
