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

def main():
    subprocess.run(["python3", "random.rfc", "|", "less"])

# Generate random number for RFC url
rand_num = random.randint(0, 9260)

# Ask for desired direction
user_input = input("Would you like a random RFC? y/n: ")

if user_input == 'X' or 'x':
    # Get user input for custome RFC
    user_input = input("What number RFC would you like? Select between 1 - 9260: ")
    rfc = "https://www.rfc-editor.org/rfc/rfc" + user_input + '.txt'
    rfc_url = urllib.request.urlopen(rfc)
else:
    # Create initial RFC url
    rfc = "https://www.rfc-editor.org/rfc/rfc" + str(rand_num) + '.txt'
    rfc_url = urllib.request.urlopen(rfc)

# Display RFC
for line in rfc_url:
    print(line.decode("utf-8").rstrip())


# TODO: Add specific RFC if desired function
# TODO: Figure out how to pipe print to less shell command

# Process output to 'less' command in shell

subprocess.run(["less"], capture_output=True)
# subprocess.run(['less'], stdout=subprocess.PIPE, input=rfc_url.read().decode('utf-8'), shell= True, text=True).stdout

if __name__ == "__main__":
    main()
