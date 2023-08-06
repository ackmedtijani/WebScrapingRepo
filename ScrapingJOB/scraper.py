import bs4
import requests
import pandas as pd
import numpy as np
import boto3
import matplotlib.pyplot as plt


def get_basketball_stats(link='https://en.wikipedia.org/wiki/Michael_Jordan'):
    # read the webpage 
    response = requests.get(link)
    # create a BeautifulSoup object to parse the HTML  
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # the player stats are defined  with the attribute CSS class set to 'wikitable sortable'; 
    #therefore we create a tag object "table"
    table=soup.find(class_='wikitable sortable')

    #the headers of the table are the first table row (tr) we create a tag object that has the first row  
    headers=table.tr
    #the table column names are displayed  as an abbreviation; therefore we find all the abbr tags and returs an Iterator
    titles=headers.find_all("abbr")
    #we create a dictionary  and pass the table headers as the keys 
    data = {title['title']:[] for title in titles}
   #we will store each column as a list in a dictionary, the header of the column will be the dictionary key 

    #we iterate over each table row by fining each table tag tr and assign it to the objed
    for row in table.find_all('tr')[1:]:
    
        #we iterate over each cell in the table, as each cell corresponds to a different column we all obtain the correspondin key corresponding the column n 
        for key,a in zip(data.keys(),row.find_all("td")[2:]):
            # we append each elment and strip any extra HTML contnet 
            data[key].append(''.join(c for c in a.text if (c.isdigit() or c == ".")))

    # we remove extra rows by finding the smallest list     
    Min=min([len(x)  for x in data.values()])
    #we convert the elements in the key to floats 
    for key in data.keys():
    
        data[key]=list(map(lambda x: float(x), data[key][:Min]))
       
    return data

mj_dict=get_basketball_stats(links[0])
kb_dict=get_basketball_stats(links[1])
lj_dict=get_basketball_stats(links[2])
sc_dict=get_basketball_stats(links[3])

mj_pd = pd.DataFrame(mj_dict)
kb_pd = pd.DataFrame(kb_dict)
lj_pd = pd.DataFrame(lj_dict)
sc_pd = pd.DataFrame(sc_dict)

dataframe = [mj_pd, kb_pd , lj_pd , sc_pd]

def plot(df , name):
    plt.plot(df[['Points per game']],label=name)
    plt.legend()
    plt.xlabel('Years')
    plt.ylabel('Points per game')

def save_to_csv(name):
    csv_name = f"SC1-{name}.csv"
    df.to_csv(csv_name) 

i = 0
for name in names:
    current_dict=get_basketball_stats(links[i])
    df = pd.DataFrame(current_dict)
    print(name)
    print(df.head(5))
    print(" \n")
    i+=1
    
    #PLOTS FOR EACH DATA FRAME
    plot(df ,name)
    
    #sAVES TO THE CSV
    save_to_csv(name)

    
