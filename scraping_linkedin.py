import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class Experience:
    def __init__(self , content):
        self.content = content.findAll('div' , class_ = "profile-section-card__contents")
    
    
    def all(self):
        
        dicts = {
            self.get_company(i) : \
                [
                self.get_title(i),
                self.get_timeline(i) for i in self.content
            ]
            
        }
        
        return dicts
            
            
    @staticmethod
    def get_company(con):
        company = con.find('a' , class_ = "profile-section-card__subtitle-link")
        if company is None:
            company = con.find('a' , class_ = "profile-section-card__subtitle")
        return company.text.strip()
    
    @staticmethod
    def get_timeline(content):
        start_time = [i.text for i in content.findAll('time')]
        span = content.find('span' , class_="before:middot").text
        if len(start_time) < 2:
            present = 'present'
            return f"{start_time[0]} to Present - {span}"
        return f"{start_time[0]} to {start_time[1]} - {span}"
    
    
    @staticmethod
    def get_title(content):
        return content.find('h3' , 'profile-section-card__title').text.strip()
    
    

class Details:
    
    def __init__(self , content):
        self.content = BeautifulSoup(content , 'html.parser')
    
    @property
    def get_name(self):
        return self.content.find('h1' , class_ = "top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0").text
     
    @property
    def get_experience(self):
        return Experience(self.content.find('section' , class_ = "experience"))

def main():
    
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=op)
    driver.implicitly_wait(3)
    driver.get("https://www.linkedin.com/in/tijani-ahmed-oboirien-4a3b9b209/")
    
    
    
    time.sleep(1)
    d = Details(driver.page_source)
    
    return d.get_experience.all()
    
    
    
    


print(main())