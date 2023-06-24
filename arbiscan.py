
#mind donating SRAVstudios
#BTC - bc1q5kmqqynratseyh7v0n8q58rn7p5xejuemmc4px

#USDT(ETH) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#USDT(SOLANA) - 4MjmiAwiQT1cqb5fSpvdsKCabZAKxopcMsTqem9gWBqB

#USDT(POLYGON) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#ETH - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

import requests
from bs4 import BeautifulSoup 

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}) 
 
url = 'https://arbiscan.io/'

response = requests.get(url, headers = HEADERS) 
soup = BeautifulSoup(response.content, "html.parser") 

#mind donating SRAVstudios
#BTC - bc1q5kmqqynratseyh7v0n8q58rn7p5xejuemmc4px

#USDT(ETH) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#USDT(SOLANA) - 4MjmiAwiQT1cqb5fSpvdsKCabZAKxopcMsTqem9gWBqB

#USDT(POLYGON) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#ETH - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572
etherprice = soup.find_all("a", attrs={'href':'/chart/etherprice'}) 
print(etherprice[0].text)
