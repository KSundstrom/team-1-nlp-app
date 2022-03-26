#!/usr/bin/env python3


from bs4 import BeautifulSoup
import requests
from datetime import date
import json


HTML_PAGE = requests.get('https://en.ilmatieteenlaitos.fi/weather-and-sea')


# Get the web page and select the appropriate div
soup = BeautifulSoup(HTML_PAGE.content, 'html.parser')
select = soup.find('div', class_="col-lg-9 px-0")

# Name the tags we want to extract from the div that we set earlier
wanted_tags = ["h1", "h2", "h3", "p"]
h1_list = []
h2_list = []
h3_list = []
p_list = []

# Separate the plain text by tag to lists
for tag in wanted_tags:
    for instance in soup.find_all(tag):
       #print(f"{instance.name} -> {instance.text.strip()}")
        if tag == "h1":
            h1_list.append(instance.text.strip())

        if tag == "h2":
            h2_list.append(instance.text.strip())
        if tag == "h3":
            h3_list.append(instance.text.strip())
        if tag == "p":
            p_list.append(instance.text.strip())

title = h1_list[0]
warnings_forecasts = h2_list[:-1]
places = h3_list[:-7]
forecasts_text = p_list[1:-8]

seen_before = []
entries = []
for item in places:
    forecast = {}
    forecast['date'] = date.today().strftime("%d/%m/%Y")
    forecast['title'] = title
    forecast['place'] = item
    if seen_before:
        forecast['forecast'] = "forecast"
    else:
        forecast['forecast'] = "warning"
        if item.lower() == "inference":
            seen_before.append(item)
    forecast['forecast text'] = forecasts_text[places.index(item)]
    entries.append(forecast)

entries_json = json.dumps(entries, indent = 4)
print(entries_json)
#print(seen_before)
#print(title)
#print(warnings_forecasts)
#print(len(places))
#print(len(forecasts_text))

#print(h1_list)
#print(h2_list)
#print(h3_list)
#print(p_list)
