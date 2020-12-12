# address : https://www.espncricinfo.com/ci/content/player/index.html
# player info : http://search.espncricinfo.com/

import requests
from bs4 import BeautifulSoup

search_URL = "http://search.espncricinfo.com/ci/content/player/search.html?search="
info_URL = "http://search.espncricinfo.com/"
player_name = "Tamim Iqbal"

response = requests.get(search_URL+player_name)
serach_page = BeautifulSoup(response.content, 'html5lib')

player_unique_tag = serach_page.find('a', attrs={'class': "ColumnistSmry"})
player_url = player_unique_tag['href']

response = requests.get(info_URL+player_url)
player_page = BeautifulSoup(response.content, 'html5lib')
# print(soup.prettify())


player_info = player_page.findAll('p', attrs={"class": "ciPlayerinformationtxt"})

# print(table[1].span)
for info in player_info:
    if "Playing role" in info.b or "Batting style" in info.b or "Bowling style" in info.b:
        print(f"{info.b.string}: {info.span.string}")
    
