import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
table = soup.find('table',class_="ih-td-tab auction-tbl")
Header = []
data = table.find_all("th")
for i in data:
    head = i.text
    Header.append(head)
df = pd.DataFrame(columns=Header)
rows = table.find_all("tr")
for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row = [tr.text for tr in data]
    row.insert(0,first_td)
    l = len(df)
    df.loc[l]= row
df.to_csv("IPL_auction_2022.csv")



