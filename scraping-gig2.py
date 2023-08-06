"""
    A python scripts that scraps through the har.com website to find house images and other metadata such
    as the bedroom numbers, bathroom sizes, square kilometers and lot size

    Returns:
        _type_: _description_
"""


import requests
import pprint
from bs4 import BeautifulSoup

url = "https://www.har.com/homedetail/"
strs = "14723 Earlswood Dr, Houston, TX 77083"
product_name = "14723-earlswood-dr-houston-tx-77083/2480964"

absolute_url = [f"{url}{product_name}"]


def preprocess_string(strs):
    return strs.strip().lower().replace(",")

'''
def find_requirements(url):
    res = req.get(url)
    content = BeautifulSoup(res.text , 'html.parser')
    return content
'''

def find_img(content):
    """Returns the url to the house image

    Args:
        content (_type_): _description_

    Returns:
        _type_: _description_
    """
    img = content.find('div' , class_ = "pd_banner_item_inner").find('img')['data-lazy']
    return img
    
def find_traverse(content):
    
    return content.find_all('div' , class_ = "col-md-4 col-6 pb-2")[:-1]
    
def find_bedroom(content):
    print(content.find('span').text.strip())
    return f"{content.find('span').text.strip()} Bathrooms"

def find_bathroom(content):
    content = content.find_all('span')
    return f"{content[0].text} Full {content[1].text} Bath"

def find_sqrt(content):
    return f"{content.find('span' , class_= 'font_weight--bold').text} Sqrts"

def find_lot(content):
     return f"{content.find('span' , class_= 'font_weight--bold').text} Lots"

def main():
    with requests.Session() as req:
        for i in absolute_url:
            res = req.get(i)
            content = BeautifulSoup(res.text , 'html.parser')
            print(find_img(content))
            contents = find_traverse(content)
            print(find_bedroom(contents[0]))
            print(find_bathroom(contents[1]))
            print(find_sqrt(contents[2]))
            print(find_lot(contents[3]))

main()
            