import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# get the html page using requests and beautifulsoap
url = 'http://45.56.117.197/index.html'
html_page = requests.get(url)
print(html_page)
soup = BeautifulSoup(html_page.text, 'html.parser')

userInfoDom = soup.find(class_='text-gray-700')
 #get the section of html page with user info


print("processing")

df_login = pd.DataFrame(columns=['Login ID', 'Repo Count', 'Follower Count', 'Member Since']) 
# pandas dataframe to store the data and later convert to csv

#get the user info
for content in userInfoDom.find_all(class_='grid-cols-4')[1:]:
    userInfo = []
    for info in content.find_all('div'):
        
        userInfo.append(info.get_text(strip=True))
    #userInfo[2] = re.sub(" \*+", " ", userInfo[2])
    df = pd.DataFrame([[userInfo[0],userInfo[1],userInfo[2],userInfo[3]]], columns=df_login.columns)
    df_login = df_login.append(df) 
    
#removing invalid data(removing the data which Repo colum=-1 ;i found that user has alo -1 in follower count and 0 in Member_since who has -1 in Repo )

df_login = df_login[df_login['Repo Count'] != str(-1)]

df_login.drop_duplicates().to_csv('/Users/krishnasharma/desktop/econ8060/midterm_1/part1.csv', index=False) 
#drop duplicates and store in csv

#checkig for validity- comparing the information with original dataset
dataset = pd.read_csv("/Users/krishnasharma/desktop/econ8060/midterm_1/part1.csv")

print(dataset)
print(dataset.describe())


print("done")