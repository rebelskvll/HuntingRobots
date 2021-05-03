import sys
import argparse
import requests
from urllib import request
import re

# Args for the command line help
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="URL for hunting the robots.txt")
args = parser.parse_args()

# Check if the url in robots.txt is available or not, and print error code in case of not.
def checkcode(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("There may be something interesting in", url)
    else:
        print("We got some trouble in", url, "status code", str(response.status_code))


# If don't get the url arg, shows help and exit
if len(sys.argv) < 2:
    print(parser.print_help())

# Try to establish connection to the url, and print some information or exit in case of unhandled exception
try:
    response = requests.get(args.url)
    if response.status_code == 200:
        print("Host online, happy hunting")
    else:
        print("Something went wrong, status code", str(response.status_code))
except:
    print("Can't reach the host or maybe is down")
    sys.exit()

# URL
robots_url = args.url + "/robots.txt"

# Check the given url for robots file. Exit if can't find it
response = requests.get(robots_url)
if response.status_code != 200:
    print("Bad luck, no robots in", args.url)
    sys.exit()
else:
    print("OK, robots.txt found. Open season")


# Open the file, convert to string and remove blank spaces and other characters
# With a regex find the paths in disallow section in robots.txt
# And remove other residual characters
file = request.urlopen(robots_url)
for line in file:
    line = line.strip()
    line = str(line)
    line = re.sub(r"\s+", "", line)
    regex = re.findall('Dis.*:(/\S*)', str(line))
    finalstring = ''.join(regex)
    finalstring = finalstring.replace(": ", "")
    if len(regex) > 0:
        finalstring = finalstring.replace("'", "")
        checkcode(args.url+finalstring)
