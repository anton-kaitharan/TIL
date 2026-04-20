import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.commodityonline.com/mandiprices/coconut-oil/kerala')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.title)

# content = soup.find('div', class_='mandi_highlight')
# if content:
#     for para in content.find_all('h4'):
#         print(para.text.strip())
# else:
#     print("No content found")