import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import json
import time


f = open("github_id", "r")
token = f.read()
f.close()

f = open("api_key", "r")
username = f.read()
f.close()


github_session = requests.Session()
github_session.auth = (username, token)



access_point = "https://api.github.com"

# # # Check Rate Limit
rate_limit_url = access_point + "/rate_limit"
result = json.loads(github_session.get(rate_limit_url).text)
#print(result)

df_1 = pd.DataFrame(columns=['avatar_url','url','following', 'followers', 'count_starred','public_repos','name', 'company','blog' ,'location','email' ,'hireable' ,'bio','created_at','updated_at']) 
df_userinfo = pd.read_csv("/Users/krishnasharma/desktop/econ8060/midterm_1/part1.csv")
#print(df_userinfo)


for i, row in df_userinfo[0:101].iterrows(): 
	user_url = access_point + "/users/" + row['Login ID']
	#print(user_url)
	try:
		json_response = json.loads(github_session.get(user_url).text)
		#print(json_response)
		#print('.............................................')
		avatar_url=json_response['avatar_url']
		url = access_point + "/users/" + row['Login ID']
		following = json_response['following']
		follower=json_response['followers']
		count_starred = len(json.loads(github_session.get(user_url + "/starred").text))
		public_repos =json_response['public_repos']
		name=json_response['name']
		company=json_response['company']
		location=json_response['location']
		blog =json_response['blog']
		hireable=json_response['hireable']
		bio=json_response['bio']
		email=json_response['email']
		created_at=json_response['created_at']
		updated_at=json_response['updated_at']
		time.sleep(5)

		df = pd.DataFrame([[ avatar_url,url,following, follower,count_starred,public_repos, name, company,blog,location,email ,hireable,bio,created_at,updated_at]],columns=df_1.columns)
		df_1 = df_1.append(df) 
	except:
		continue

df_1.to_csv("/Users/krishnasharma/desktop/econ8060/midterm_1/part2_3/part2_dataset.csv", index=False)
print("done")




