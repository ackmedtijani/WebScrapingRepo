#Scrapping hotel  reviews per project


from bs4 import BeautifulSoup
import requests
import pprint
import argparse

import time


time.sleep(60)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

url = "https://euro.expedia.net/Hotel-Search?adults=2&d1=2023-06-23&d2=2023-06-24&destination=London%20%28and%20vicinity%29%2C%20England%2C%20United%20Kingdom&endDate=2023-06-24&latLong=51.507538%2C-0.127804&regionId=178279&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2023-06-23&theme=&useRewards=false&userIntent="
response = requests.get(url , headers=headers)
bs5 = BeautifulSoup(response.content , 'html.parser')
container = bs5.find_all('div' , class_="uitk-spacing uitk-spacing-margin-blockstart-three")


def getHotelName(container):
    return container.find('h4').text

def getHotelRatings():
    return container.find('span' , class_ = 'is-visually-hidden')

def getHotelPrice():
    return container.find('div' , class_='uitk-text uitk-type-600 uitk-type-bold uitk-text-emphasis-theme').text

def main():
    for contain in container:
        print(getHotelName(contain))
    
main()
