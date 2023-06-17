from bs4 import BeautifulSoup
import requests
import os.path

headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0 Win64 x64 rv:88.0) Gecko/20100101 Firefox/88.0'}

class Fight:
  def __init__(self, fighter1, record1, fighter2, record2):
    self.fighter1 = fighter1
    self.record1 = record1
    self.fighter2 = fighter2
    self.record2 = record2

  def __str__(self):
    return f"{self.fighter1}{self.record1}\n  {self.fighter2}{self.record2}"    

allRecords = []
leftFighters = []
leftFightersRecords = []
rightFighters = []
rightFightersRecords = []

def formatRecords():
    maxIndex = len(allRecords) - 1
    index = 0
    while(index < maxIndex): 
        if (index % 2) == 0:
            rightFightersRecords.append(allRecords[index])
        else:
            leftFightersRecords.append(allRecords[index])
        index = index + 1

def convertBs4ToString(bs4_array, List, type):
    if(type == 'records'):
        for data in bs4_array:
            record = data.get_text().strip()
            List.append("(" + record + ")")
            formatRecords()
    else:
        for data in bs4_array:
            List.append(data.get_text().strip())

def createFight():
    index = 0
    maxIndex = len(leftFighters) - 1
    while index < maxIndex:
        fighter1 = leftFighters[index]
        record1 = leftFightersRecords[index]
        fighter2 = rightFighters[index]
        record2 = rightFightersRecords[index]
        fight = Fight(fighter1, record1, fighter2, record2)
        print(fight)
        index = index + 1

def web_scraper(url):
    page = requests.get(url, headers=headers)
    if page.status_code != 200:
        print("Page not found.")
    else:       
        soup = BeautifulSoup(page.content, 'html.parser')
    
    try:
        bs4LeftFighters = soup.find_all("div", "fightCardFighterName left")        
        convertBs4ToString(bs4LeftFighters, leftFighters, 'fighters')
        bs4RightFighters = soup.find_all("div", "fightCardFighterName right")
        convertBs4ToString(bs4RightFighters, rightFighters, 'fighters')
        bs4Records = soup.find_all("div", "fightCardRecord")
        convertBs4ToString(bs4Records, allRecords, 'records')
        createFight()
    except AttributeError:
        print("Issue getting data.")

url = input("\nEnter Tapology Url: ")
web_scraper(url)