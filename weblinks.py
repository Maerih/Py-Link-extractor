import requests
from bs4 import BeautifulSoup
url = input("Input url to get links:")
req = requests.get(url).content
soup = BeautifulSoup(req,"html.parser")
links = soup.find_all('a')
for link in links:
    print(link['href'])
