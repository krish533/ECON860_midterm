
import requests
import pandas as pd
import json


f = open("github_id", "r")
token = f.read()
f.close()

f = open("api_key", "r")
username = f.read()
f.close()

github_session = requests.Session()
github_session.auth = (username, token)

access_point = "https://api.github.com"
df_userinfo = pd.read_csv("/Users/krishnasharma/desktop/econ8060/midterm_1/part1.csv")
print("done")
#can increase the number of user by increasing the numebr 5 to more in [0:5]
for i, row in df_userinfo[0:5].iterrows(): 
	user_url = access_point + "/users/" + row['Login ID']
	#print(user_url)
	try:
		json_response = json.loads(github_session.get(user_url).text)
		#print(json_response)	
		followers_url= json_response['followers_url']
		result=json.loads(github_session.get(followers_url).text)
		followers=[ item['login'] for item in result ]

		df_follower = pd.DataFrame()
		#for bonus point: getting the information about followers of user
		for follower in followers:
			follower_url = access_point + "/users/" + follower
			result_follower = json.loads(github_session.get(follower_url).text)
			df_follower = df_follower.append({
			'follower_id' : follower,
			'repos_count' : result_follower['public_repos'],
			'followers_count' : result_follower['followers'],
			'following_count' : result_follower['following'],
			'created_at' : result_follower['created_at'],
			'updated_at' : result_follower['updated_at']
			}, ignore_index = True)

		df_follower.to_csv("/Users/krishnasharma/desktop/econ8060/midterm_1/part2_3/part2_bonus/"+row['Login ID']+"_followers.csv")
		time.sleep(5)
	except:
		continue


