import argparse
import requests
import sys

# Args for the command line help
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='URL for hunting the robots.txt')
args = parser.parse_args()

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
        if (checkconnection(f'{args.url}/robots.txt')):
            print ('[+] We found robots c[○┬●]כ, happy hunting!')
            checkrobot(f'{args.url}/robots.txt')
        else:
            print ('[!] No robots this time')
    else:
        print ('[!] Host is down or maybe has some trouble')

def checkrobot(robotsurl):
    response = requests.get(robotsurl)
    content = response.text
    
    for line in enumerate(content.split('\n')):
        if ("Disallow: " in line[1]):
            splited = line[1].split(" ")
            response = requests.get(f'{args.url}{splited[1]}')
            if response.status_code == 200:
                print(f'{args.url}{splited[1]}')



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(parser.print_help())
    else:
        main()