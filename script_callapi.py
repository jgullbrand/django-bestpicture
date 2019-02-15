import requests
import json

r = requests.get('https://jgbestpicture.herokuapp.com/api/moviedata/')
print(f'Status Code is: {r.status_code}\n')

response_date = r.json()
Data_list = response_date["results"]
for items in Data_list:
	print(f'Movie Title: {items["title"]}\nScore: {items["score"]}\nReason for choice: {items["choice_explanation"]}\n')

