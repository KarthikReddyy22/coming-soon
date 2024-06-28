import requests
from bs4 import BeautifulSoup

def comingsoon(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    lm = soup.find('div', id="coming-soon-carousel")
    coming = lm.select('h3')
    print("\nComing soon movies...""\n" )
    for i in coming:
        print(i.get_text())
        print("\n")

comingsoon('https://www.fandango.com/')
