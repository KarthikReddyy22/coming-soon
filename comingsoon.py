import requests
from bs4 import BeautifulSoup
import schedule, time
from discordwebhook import Discord

def comingsoon():
    urls = 'https://www.fandango.com/'
    discord = Discord(url="Your discord web hook url here")
    res = requests.get(urls)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    lm = soup.find('div', id="coming-soon-carousel")
    coming = lm.select('h3')
    #print("\nComing soon movies...""\n" )
    discord.post(content="Coming soon movies...")
    discord.post(content="----------------------------")
    for i in coming:
        #print(i.get_text())
        #print("\n")
        discord.post(
            content=i.get_text()
            )
        
schedule.every().day.at('Time to post everyday').do(comingsoon)
while True:
    schedule.run_pending()
    time.sleep(1)
