from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)
page = html.fromstring(data.text)

xpath = '//div[@class="media-module__body relative"]//a//@href'

# iterowanie przez odnalezione elementy i wyświetlenie nazw i wartości atrybutów
foundElements = page.xpath(xpath)
print(foundElements)

# Chyba nie do końca o to chodziło