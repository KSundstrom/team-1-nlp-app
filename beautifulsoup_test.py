#!/usr/bin/env python3


from urllib import request
from bs4 import BeautifulSoup


def main():
    # Access FMI's website and download the raw site data of the weather forecast for shipping in English
    url = "https://en.ilmatieteenlaitos.fi/weather-forecast-for-shipping"
    html = request.urlopen(url).read().decode('utf8')

    # Run the raw HTML through BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Access the main body of the weather report through css-classes
    #texts = soup.find_all('p')
    #for text in texts:
    #    print(text.get_text())
    forecast = soup.find(id = 'proxyId_1NG1s0PovRLtQcAthgOmNp')
    print(forecast.get_text())


if __name__ == '__main__':
    main()
