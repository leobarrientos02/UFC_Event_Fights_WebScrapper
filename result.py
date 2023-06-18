from bs4 import BeautifulSoup
import requests

headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0 Win64 x64 rv:88.0) Gecko/20100101 Firefox/88.0'}

def web_scraper(url):
    page = requests.get(url, headers=headers)
    if page.status_code != 200:
        print("Page not found.")
    else:       
        soup = BeautifulSoup(page.content, 'html.parser')
    
    try:
        bs4_winners = soup.find_all("div", "fightCardFighterName left")
        print("Winners")
        print("-------")
        for x in bs4_winners:
            winner = x.get_text().strip()
            print(winner)
    except AttributeError:
        print("Winners not found")

    print()
    
    try:
        bs4_losers = soup.find_all("div", "fightCardFighterName right")
        print("Losers")
        print("------")
        for x in bs4_losers:
            loser = x.get_text().strip()
            print(loser)
    except AttributeError:
        print("Losers not found")
    
    print()
    
    try:
        bs4_results = soup.find_all("span", "result")
        print("Results")
        print("------")
        for x in bs4_results:
            result = x.get_text().strip()
            print(result)
    except AttributeError:
        print("Results not found")

url = input("\nEnter Tapology Url: ")
web_scraper(url)