import requests
from bs4 import BeautifulSoup

def haber_linklerini_getir(sayfa_url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(sayfa_url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    haber_listesi = soup.find_all("div", {"class": "f-cat f-item"})

    for i in haber_listesi:
        print("===================================")
        for b in i.find_all("ul", {"class": "list underline"}):
            for link in b.find_all('a'):
                my_link = link.get('href')
                tam_link = f"https://www.milligazete.com.tr{my_link}"
                print(tam_link)
                with open('ist.txt', 'a', encoding="utf-8") as file:
                    file.write(tam_link + "\n")

listem = [
    'https://www.milligazete.com.tr/arsiv/2025-03-22',
    'https://www.milligazete.com.tr/arsiv/2025-03-23',
    'https://www.milligazete.com.tr/arsiv/2025-03-24',
    'https://www.milligazete.com.tr/arsiv/2025-03-25',
    'https://www.milligazete.com.tr/arsiv/2025-03-26'
]

for s in listem:
    haber_linklerini_getir(s)
