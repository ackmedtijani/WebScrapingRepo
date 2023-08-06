import requests
import time
from bs4 import BeautifulSoup


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options




response = requests.Session()
NUMBER = "WAC2390054340"
URL = "https://egov.uscis.gov/"

def increment_number(num):
    return int(num[3:]) + 5
    

def client(number):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    driver.get("https://egov.uscis.gov/")
    search_field = driver.find_element(By.TAG_NAME, "input")
    search_field.send_keys(NUMBER)
    search_field.send_keys(Keys.ENTER)
    time.sleep(1)
    
    return driver.page_source

def immigration_status(content):
    content = BeautifulSoup(content , 'html.parser')
    content = content.find('h2', id = 'landing-page-header').text
    
    if 'rejected' in content.lower():
        return "Rejected"
    return "Approved"


def main():
    i = 0
    num = NUMBER
    while i < 10:
        number = "WAC" + str(increment_number(num))
        num = number
        i += 1
        yield number , immigration_status(client(number))
     
start = time.time()

for number , value in main():
    print(f"{number} Immigration status - {value}")
elapsed_time = time.time() - start

print("Elapsed time" , elapsed_time)
        
