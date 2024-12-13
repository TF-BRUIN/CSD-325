import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")

def test_API_code():
	API_status_code = response.status_code
	print(API_status_code)

def test_API_output():
	print(response.json())
	API_JSON_table = response.json()
	print(API_JSON_table)

def list_API():
	API_JSON_table = response.json()
	listed_API = 0
	for i in API_JSON_table["people"]:
		print(i)

#test_API_code()
#test_API_output()
list_API()



