import os, sys, requests, time, os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

def curl_root_me(): 
    list_root_me_usernames = os.environ.get('ROOTME_USERNAMES').split(',')
    for username in list_root_me_usernames:
        print(username)
        root_me_url_regex = 'https://www.root-me.org/' + username
        response = requests.get(root_me_url_regex)
        soup = BeautifulSoup(response.text, 'html.parser')
        for div in soup.find_all('div', class_='small-6 medium-3 columns text-center'):
            if "classement" in div.h3.img['src']:
                print("Rank :" + str(div.h3.text))
            elif "valid" in div.h3.img['src']:
                print("Points :" + str(div.h3.text))
            elif "rubon5" in div.h3.img['src']:
                print("Challenges Solved :" + str(div.h3.text))
            elif "rubon196" in div.h3.img['src']:
                print("Compromissions :" + str(div.h3.text))
            else : 
                continue
        time.sleep(1)
        print("\n")

if __name__ == '__main__':
    curl_root_me()