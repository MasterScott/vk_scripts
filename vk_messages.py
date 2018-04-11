#!/usr/bin/python3

import requests
import json
from time import sleep

v=5.52
token = 'Your token'
user_id = 415577518

def write_json(data):
	with open('messages.json', 'w') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)



def main():

		r = requests.get('https://api.vk.com/method/messages.getDialogs?', params={'count': 200, 'offset': 0, 'out': 1, 'access_token': token, 'v': v})

		item = r.json()['response']['items']

	write_json(item)

	


if __name__ == '__main__':
	main()
