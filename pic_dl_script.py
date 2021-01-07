from bs4 import BeautifulSoup as BSHTML
import urllib.request
import urllib3
import dload

http = urllib3.PoolManager()
url = input("Enter URL: ")

response = http.request('GET', url)
soup = BSHTML(response.data, "html.parser")
images = soup.findAll('img')

for image in images:
    imgLink = 'https:' + image['src']
    #print(imgLink)
    dload.save(imgLink)