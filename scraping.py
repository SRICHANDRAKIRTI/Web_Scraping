import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://books.toscrape.com/'
req=requests.get(url)
soup=BeautifulSoup(req.text,'html.parser')
Data=soup.find_all('img')
img=[]
for i in Data:
    frame=img.append({
        'SRC':i.get('src'),
        'ALT':i.get('alt'),
        'THUMNIL':i.get('class')
    })
df=pd.DataFrame(img)
print(df)
df.to_csv(r'C:\Users\DELL\Desktop\Web_scraping\scrapping_data.csv',index=False)