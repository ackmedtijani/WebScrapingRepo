import requests
from bs4 import BeautifulSoup

'''
    A bot that checks if a product in beautyexpert.com e-commerce website is out of stock'
    
'''

url = [
    'https://www.beautyexpert.com/avant-skincare-hyaluronic-acid-replenishing-lip-serum-8.5ml/11975774.html?out-of-stock-alternative',
    'https://www.beautyexpert.com/instant-effects-instant-lip-plumper/11185616.html?switchcurrency=GBP&shippingcountry=GB&utm_source=AWin-1098883&utm_medium=affiliate&utm_campaign=AffiliateWin%7CFeed&affil=awin&utm_content=https%3A%2F%2Fbeauty.earneco.io&utm_term=Editorial+Content&utm_source=AWin-1098883&utm_medium=affiliate&utm_campaign=AffiliateWin&awc=988_1688462572_7509b5b583cedd366d2b00a2ee209608'
]
# A function that checks if it's out of stock

def check_stock(url):
    with requests.Session() as session:
        response = session.get(url)
        bs4 = BeautifulSoup(response.content , 'html.parser')
        if bs4.find('h2' , class_ = 'productAlternativesWrapper_title'):
            return True
        return False
            
    

def main():
    for _ in url:
        print(f"{url} has no stocks? {check_stock(_)}")

main()