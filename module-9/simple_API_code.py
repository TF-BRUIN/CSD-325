import requests
import json

API_url = "https://www.dnd5eapi.co/api/classes/"
response = requests.get(API_url)
JSON_table = response.json()

def test_API_connection():
	API_status_code = response.status_code
	print(API_status_code)

def response_no_format():
	print(JSON_table)

def response_w_format():
	printed_lines = 0
	for i in JSON_table["results"]:
		printed_class = JSON_table["results"][printed_lines]
		print(printed_class)
		printed_lines += 1
		

test_API_connection()
print("")
response_no_format()
print("")
response_w_format()