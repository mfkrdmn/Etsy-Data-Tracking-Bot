from time import time
import requests 
from bs4 import BeautifulSoup
import time


url1 = 'https://www.etsy.com/listing/805486564/personalized-handmade-vintage-leather?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=leather+bag+men&ref=sr_gallery-1-23&pro=1&frs=1&organic_search_click=1'


headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

page = requests.get(url1, headers=headers)

htmlPage = BeautifulSoup(page.content,'html.parser')

productTitle = htmlPage.find('h1', class_='wt-text-body-03 wt-line-height-tight wt-break-word').getText()
price = htmlPage.find('p', class_='wt-text-title-03 wt-mr-xs-2').getText()

price = "US$125.91+"

convertedPrice = float(price.replace("US","").replace("$","").replace("+",""))

if(convertedPrice >= 110):
      print('fiyat dustu')
else:
       print('fiyat dusmedi')

print(convertedPrice)




#while(True):
 #   checkPrice(url1,450)
  #  time.sleep(10)