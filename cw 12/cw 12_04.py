from bs4 import BeautifulSoup
import urllib3
import pandas as pd


url = "https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed"
http = urllib3.PoolManager()
page = http.request("GET", url)
# wyświetla każdy odczytany bajt

soup = BeautifulSoup(page.data, 'lxml')
# zawartość strony jest sformatowana w bardziej przystepny sposób, tak jakbyśmy przeglądali źródło strony w narzędziach developerskich przeglądarki


daty = []
oceny = []
tytuly = []
platformy = []

for data in soup.find("div", {"class": "title_bump"}).find_all('div', {"class": "clamp-details"}):
        for ta in data.find_all('span'):
            if not ta.attrs.values():
                daty.append(ta.text)
for ocena in soup.find('div', {"class": "title_bump"}).find_all('div', {"class": "metascore_w large game positive"}):
        oceny.append(ocena.text)
for tytul in soup.find('div', {"class": "title_bump"}).find_all('h3'):
    tytuly.append(tytul.text)
for platforma in soup.find('div', {"class": "title_bump"}).find_all('span', {"class": "data"}):
    platformy.append(platforma.text.strip())



df = pd.DataFrame((list(zip(tytuly,platformy,daty,oceny))),columns = ['Tytul','Platforma','Data_wydania','Ocena'])

print(df)