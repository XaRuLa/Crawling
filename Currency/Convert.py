import simplejson
import requests
from bs4 import BeautifulSoup

url = 'http://www.xe.com/currencyconverter/convert/?From=USD&To=MYR' #page
source_code = requests.get(url)
status = source_code.content
soup = BeautifulSoup(status, 'lxml')
aa = soup.findAll('span', {'class':'uccResultUnit'})
for c in aa:
 Dollar = c.text.strip()
 print Dollar

