import simplejson
import requests
from bs4 import BeautifulSoup

url = 'http://www.waktusolat.org/kota-bharu-waktu-solat.html' #page
source_code = requests.get(url)
status = source_code.content
soup = BeautifulSoup(status, 'lxml')
aa = soup.findAll('ul', {'class':'sec'})
for item in aa:

 tarikh = item.contents[1].text

 timeimsak = item.contents[3].text[5] + item.contents[3].text[6] + item.contents[3].text[7] + item.contents[3].text[8] + item.contents[3].text[9]
 imsak = item.contents[3].find('span').text + '    ' + timeimsak

 timesubuh = item.contents[5].text[5] + item.contents[5].text[6] + item.contents[5].text[7] + item.contents[5].text[8] + item.contents[5].text[9]
 subuh = item.contents[5].find('span').text + '    ' + timesubuh

 timesyuruk = item.contents[7].text[6] + item.contents[7].text[7] + item.contents[7].text[8] + item.contents[7].text[9] + item.contents[7].text[10]
 syuruk = item.contents[7].find('span').text + '   ' + timesyuruk

 timezohor = item.contents[9].text[5] + item.contents[9].text[6] + item.contents[9].text[7] + item.contents[9].text[8] + item.contents[9].text[9]
 zohor = item.contents[9].find('span').text + '    ' + timezohor

 timeasar = item.contents[11].text[4] + item.contents[11].text[5] + item.contents[11].text[6] + item.contents[11].text[7] + item.contents[11].text[8]
 asar = item.contents[11].find('span').text + '     ' + timeasar

 timemaghrib = item.contents[13].text[7] + item.contents[13].text[8] + item.contents[13].text[9] + item.contents[13].text[10] + item.contents[13].text[11]
 maghrib = item.contents[13].find('span').text + '  ' + timemaghrib

 timeisyak = item.contents[15].text[5] + item.contents[15].text[6] + item.contents[15].text[7] + item.contents[15].text[8] + item.contents[15].text[9]
 isyak = item.contents[15].find('span').text + '    ' + timeisyak

 print tarikh
 print imsak
 print subuh
 print syuruk
 print zohor
 print asar
 print maghrib
 print isyak
 print '  '
 print '  '


 dataa = {'Tarikh':tarikh,'Imsak':timeimsak,'Subuh':timesubuh,'Syuruk':timesyuruk,'Zohor':timezohor,'Asar':timeasar,'Maghrib':timemaghrib,'Isyak':timeisyak}
 data = simplejson.dumps(dataa)
 print data


