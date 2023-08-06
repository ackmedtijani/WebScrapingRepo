import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
 
# connect to google.com
'''
driver = webdriver.Chrome(options=Options())
driver.get("https://www.google.com")
 
# find the search input field
search_field = driver.find_element(By.TAG_NAME, "textarea")
 
# type the search string
search_field.send_keys("selenium")
 
# send enter key to get the search results!
search_field.send_keys(Keys.ENTER)
'''
params = {
    'q' : 'selenium'
}

search = requests.get('https://www.google.com/search?q=Selenium')

bs4 = BeautifulSoup(search.content , "html.parser")
print(bs4.find('div',  {'id' : 'main'}))

class FaceBookBot:
    login_basic_url = 'https://www.facebook.com/login'
    login_mobile_url = 'https://m.facebook.com/login'
    payload = {
            'email': os.getenv('FB_USERNAME'),
            'pass': os.getenv('FB_PASSWORD')
        }
    post_ID = ""


    
    def parse_html(self, request_url):
        with requests.Session() as session:
            print(self.payload)
            post = session.post(self.login_basic_url, data=self.payload)
            print(post.status_code)
            parsed_html = session.get(request_url)
        return parsed_html
    
    
    def get_group_data(self):
        requests_url = f"https://www.facebook.com/groups/1439559239671135"
        
        class_ = "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1xlr1w8"
        
        soup = BeautifulSoup(self.parse_html(request_url=requests_url).content , 'html.parser' )
       
        
        
        

    def post_content(self):
        REQUEST_URL = f'https://mbasic.facebook.com/story.php?story_fbid={self.post_ID}&id=415518858611168'
        
        soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
        content = soup.find_all('p')
        post_content = []
        for lines in content:
            post_content.append(lines.text)
        
        post_content = ' '.join(post_content)    
        return post_content

    '''
    def date_posted(self):
        REQUEST_URL = f'https://mbasic.facebook.com/story.php?story_fbid={self.post_ID}&id=415518858611168'
        
        soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
        date_posted = soup.find('abbr')
        return date_posted.text

    def post_likes(self):
        limit = 200
        REQUEST_URL = f'https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit={limit}&total_count=17&ft_ent_identifier={self.post_ID}'

        soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
        names = soup.find_all('h3')
        people_who_liked = []
        for name in names:
            people_who_liked.append(name.text)
        people_who_liked = [i for i in people_who_liked if i] 
        return people_who_liked

    def post_shares(self):        
        REQUEST_URL = f'https://m.facebook.com/browse/shares?id={self.post_ID}'
        
        with requests.Session() as session:
            post = session.post(self.login_mobile_url, data=self.payload)
            parsed_html = session.get(REQUEST_URL)
        
        soup = BeautifulSoup(parsed_html.content, "html.parser")
        names = soup.find_all('span')
        people_who_shared = []
        for name in names:
            people_who_shared.append(name.text)
        return people_who_shared
        
    '''
    
'''
b1 = FaceBookBot()
b1.get_group_data()
'''