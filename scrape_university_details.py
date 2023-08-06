import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup


def get_driver(driver , i , department):
    driver.get(i)
    search = driver.find_element(By.CLASS_NAME , "quicksearch")
    search.click()
    lick = driver.find_element(By.CLASS_NAME , "optional")
    lick.click()
    x = driver.find_element(By.ID, "dirDept")
    driver.implicitly_wait(5)
    print(x.tag_name , x.get_attribute("class"))
    select = Select(x)
    time.sleep(4)
    select.select_by_visible_text(department)
    time.sleep(3)
    driver.find_element(By.CLASS_NAME , "allrecs").click()
    time.sleep(5)
    driver.implicitly_wait(5)
    content = BeautifulSoup(driver.page_source , 'html.parser')
    scraper(content)
    

def scraper(content):
    content = content.find("div" , id = "dirResults")
    
    if dir == []:
        print("No persons")
        return None
    else:
        print("Found page")
        content = content.findAll("div" , class_="resultPage")
        for con in content:
            try:
                find_content(con)
            except:
                print(con)
        

def find_content(content):
    
    content = content.findAll("div" , class_ = "bg-white")
    for i in content:
        print("Name" , find_name(i))

def find_name(content):
    return content.find("h2").text

def find_position(content):
    return content.find("h3").text

def main(url , department):
    
    op = webdriver.ChromeOptions()
    #op.add_argument('headless')
    op.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=op)
    
    for i in url:
        get_driver(driver ,i , department)
        


if __name__ == "__main__":
    main(["https://www.utdallas.edu/directory/"] , "Bioengineering")
       
        
        