#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

result = requests.get("https://www.newegg.com/p/pl?N=100007709%20601357247")

doc = BeautifulSoup(result.content, "html.parser")

prices  = doc.find_all(string="$")
parent = prices[0].parent

strong = parent.find("strong")
print(strong.string)
