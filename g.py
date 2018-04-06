__module_name__ = "ClawBot"
__module_version__ = "1.0"
__module_description__ = "Some shitty bot"

import hexchat

#################
import requests
from bs4 import BeautifulSoup

url = "https://www.google.co.in/search?q="
searches = []

def searching(searchz):
    r = requests.get(url + searchz)

    soup = BeautifulSoup(r.content, "lxml")

    #print(soup.prettify())

    links = soup.find_all("h3", {"class": "r"})

    for link in links:
        searches.append(link.contents[0].text + " --> " +  "http://www.google.co.in" + link.contents[0].get("href"))
        break
####################

x = " #phoenixcrusaders "

def command(word, word_eol, userdata):
    lmao = word[1].strip("!g ")
    if(word[1].startswith("!g")):
         searching(lmao)
         print(searches)
         hexchat.command("msg" + x + searches[-1])
hexchat.hook_print("Channel Message", command)

