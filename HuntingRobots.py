import sys
import argparse
import requests
from urllib import request
import re

# Args for the command line help
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='URL for hunting the robots.txt')
args = parser.parse_args()

# Check if the url in robots.txt is available or not, and print error code in case of not.
def checkconnection(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False


def main ():
    print ('[*] Checking if host is online')
    if (checkconnection(args.url)):
        print ('[+] Host is online')
        print ('[*] Checking if robots.txt is present')
        if (checkconnection(args.url+"/robots.txt")):
            print ('[+] We found a robot c[○┬●]כ, happy hunting!')
            #checkrobot()
        else:
            print ('[!] No robots this time')
    else:
        print ('[!] Host is down or maybe has some trouble')


def checkrobot():
    pass
    #file = request.urlopen(args.url+"/robots.txt")
    #for line in file:
    #    line = line.strip()
    #    line = str(line)
    #    line = re.sub(r"\s+", "", line)
    #    regex = re.findall('Dis.*:(/\S*)', str(line))
    #    finalstring = ''.join(regex)
    #    finalstring = finalstring.replace(": ", "")
    #    if len(regex) > 0:
    #        finalstring = finalstring.replace("'", "")
    #        checkcode(args.url+finalstring)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(parser.print_help())
    else:
        main()