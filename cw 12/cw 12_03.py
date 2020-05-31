from lxml import html
import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://boardgamegeek.com/browse/boardgame"
data = requests.get(url)

page = html.fromstring(data.text)
# tabela z grami wszechczasów (tylko pierwsza strona !), pobrana za pomocą XPath
xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
# można pobierać elementy dokumentu również poprzez funkcje pakietu lxml po id lub klasie
table_div = page.get_element_by_id('collection')

# w dowolnym momencie na elemencie ponownie możemy pobrać elementy przez XPath, najważniejsza jest wiedza o drzewie DOM dokumentu w celu określenia odpowiedniej ścieżki względnej lub bezwzględnej 
# należy pamiętać (lub sprawdzić) to, że zostanie zwrócona lista odnalezionych elementów dokumentu, stąd index [0] aby zwrócić bezpośrednio ten element a nie całą listę
table = table_div.xpath('./*[@class="table-responsive"]/table')[0]



# kolejna informacja jest taka, że większość (ale nie wszystkie) nagłówków jest w formie łącza (znacznik <a>), trzeba więc wyłuskać z niego tekst
headers = [label for label in table.xpath('.//th')]

labels = []
for header in headers:
    anchor = header.xpath('./a/text()')
    if len(anchor) > 0:
        # znowu anchor to lista, pozbywamy się znaków niedrukowalnych
        labels.append(anchor[0].strip())
    else:
        # trzeba pozbyć się znaków niedrukowalnych
        labels.append(header.text.strip())

labels.remove('')
labels.remove('Shop')




dane1 = table_div.xpath('//td[@class="collection_bggrating"]')

danee1 = []

for header in dane1:
    anchor = header.xpath('.//a/text()')
    if len(anchor) > 0:
         danee1.append(anchor[0].strip())
    else:
        danee1.append(header.text.strip())




dane = table_div.xpath('//tr[@id="row_"]')
danee = []

for header in dane:
    anchor = header.xpath('.//a/text()')
    if len(anchor) > 0:
         danee.append(anchor[0].strip())
    else:
        danee.append(header.text.strip())



dane2 = table_div.xpath('//td[@class="collection_rank"]')
ranking = []

for header in dane2:
    anchor = header.xpath('.//a/@name')
    if len(anchor) > 0:
        ranking.append(anchor[0].strip())
    else:
        ranking.append(header.text.strip())



geek = danee1[0:len(danee1):3]
avg = danee1[1:len(danee1):3]
num = danee1[2:len(danee1):3]

df = pd.DataFrame((list(zip(ranking,danee,geek,avg,num))),columns = labels)

df['Num Voters'] = df['Num Voters'].astype('int64')
wykres = df.nlargest(10,'Num Voters')

plt.bar(wykres['Title'],height=wykres['Num Voters'])
plt.title('10 Gier z największa liczbą recenzji')
plt.legend()

plt.show()