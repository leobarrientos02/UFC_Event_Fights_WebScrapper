from bs4 import BeautifulSoup
import requests
import os.path

headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0 Win64 x64 rv:88.0) Gecko/20100101 Firefox/88.0'}

class Fight:
  def __init__(self, fightNumber, fighter1, fighter2):
    self.fightNumber = fightNumber
    self.fighter1 = fighter1
    self.fighter2 = fighter2

def web_scraper(url):
    page = requests.get(url, headers=headers)
    if page.status_code != 200:
        print("Page not found.")
    else:       
        soup = BeautifulSoup(page.content, 'html.parser')
    
    try:
        bs4_fighters = soup.find_all("div", "fightCardFighterName left")
        print("Fighter 1")
        print("-------")
        for x in bs4_fighters:
            fighter = x.get_text().strip()
            print(fighter)
    except AttributeError:
        print("Fighter not found")  

    try:
        bs4_fighters = soup.find_all("div", "fightCardFighterName right")
        print("Fighter 2")
        print("-------")
        for x in bs4_fighters:
            fighter = x.get_text().strip()
            print(fighter)
    except AttributeError:
        print("Fighter not found")    

    try:
        bs4_records = soup.find_all("div", "fightCardRecord")
        print("Records")
        print("-------")
        for x in bs4_records:
            record = x.get_text().strip()
            print("(" + record + ")")
    except AttributeError:
        print("Records not found")

    try:
        bs4_fights = soup.find_all("div", "fightCardBoutNumber")
        print("Fight Number")
        print("-------")
        for x in bs4_fights:
            fightNumber = x.get_text().strip()
            print(fightNumber)
    except AttributeError:
        print("Fight not found")

url = input("\nEnter Tapology Url: ")
web_scraper(url)