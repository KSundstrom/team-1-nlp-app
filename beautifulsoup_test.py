from urllib import request
from bs4 import BeautifulSoup


# Access FMI's website and download the raw site data of the weather report for sailors
url = "https://www.ilmatieteenlaitos.fi/saatiedotus-merenkulkijoille"
response = request.urlopen(url)
html_doc = response.read().decode('utf8')

# Run the raw HTML through BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# Access the main body of the weather report through css-classes

#texts = soup.find_all('p')
#for text in texts:
#    print(text.get_text())

forecast = soup.find(id = 'proxyId_2eI9z8S0RBAYRYtyyE9qu8')
for text in forecast:
    print(text.get_text())
