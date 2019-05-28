import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

#url = 'https://www.dcard.tw/f'
url = 'https://booking.flypeach.com/tw/flight_search/tw/flight_search'

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.get_text())

#print(soup.span)  #got span element
#print(soup.span.string)  #got span element's sting'

#print(soup.prettify())    #pretty the element 

#a_tags = soup.select('span,cos-price')     #select the chooise element
#for t in a_tags:
#    print(a_tags)

#a_tags = soup.find_all('span')
#print(a_tags)

print(resp.status_code)
#print(resp.request.headers)
#print(resp.text.encode('utf-8', errors='ignore'))
#print(resp.encoding)
