# Import dependencies
import argparse
import requests

# Argument Parser
parser = argparse.ArgumentParser(description='Scan a given url for processed_words or directories')
parser.add_argument('mode', help='dir or sub')
parser.add_argument('-d', '--domain', required=True, help='Enter a url')
parser.add_argument('-w', '--wordlist', required=True, help='Wordlist to use')

args = parser.parse_args()

# Open the wordlist and split on lines
wordlist = open(args.wordlist).read()
processed_words = wordlist.splitlines()

# Subdomain scanner
def sub_scanner():
    for word in processed_words:
        # Add the word from the wordlist to the start of the given url
        subdomain = f"http://{word}.{args.domain}"

        # Try and request that site and see the connection outcome
        try:
            requests.get(subdomain)
        
        # If Connection Error, subdomain does not exist so move on
        except requests.ConnectionError:
            pass

        else:
            print("Valid domain: ", subdomain)

def dir_scanner():
    for word in processed_words:
        directory = f"http://{args.domain}/{word}"

        current_try = requests.get(directory)
        status = current_try.status_code
        
        print(f'Trying: {directory}       Code: {status}')

if __name__ == '__main__':
    if args.mode == 'sub':
        sub_scanner()
    elif args.mode == 'dir':
        dir_scanner()
    else:
        print("Invalid Arguments")
        exit