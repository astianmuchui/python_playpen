#!/usr/bin/env python3

from bs4 import BeautifulSoup


with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("p")[0]
b = tags.find_all("b")

print(tags)
print(b)