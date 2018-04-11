#!/usr/bin/python3

import requests
import json
from time import sleep
from random import randint


owner_id = 415577518
album_id = 243711594
chat_const = 2000000000
peer_id = chat_const +  10
token = 'Your token'
v= 5.63


def write_json(data):
	with open('photos.json', 'w') as file:
		json.dump(data, file, indent= 2, ensure_ascii=False)


def send_message(peer_id, attachment):
	r = requests.get('https://api.vk.com/method/messages.send?', params={'access_token': token,
	 																  'peer_id': peer_id,
	 																  'attachment': attachment,
	 										  						  'v': v}).json()


def main():
	offset = 1140
	all_photos = []
	number_of_photos = requests.get('https://api.vk.com/method/photos.get?', params={'owner_id': owner_id,
	 																  'access_token': token, 
	 															   	  'album_id': album_id,
	 															   	  'photo_sizes': True,
	 										 						  'count': 1,
	 										  						  'offset': offset,
	 										  						  'v': v}).json()['response']['count']
	
	while True:
		sleep(1)
		r = requests.get('https://api.vk.com/method/photos.get?', params={'owner_id': owner_id,
	 																  'access_token': token, 
	 															   	  'album_id': album_id,
	 															   	  'photo_sizes': True,
	 										 						  'count': 100,
	 										  						  'offset': offset,
	 										  						  'v': v}).json()
		photos = r['response']['items']
		all_photos.extend(photos)

		if offset >= number_of_photos:
			break

		offset+=100
		

	write_json(all_photos)
	photos = json.load(open('photos.json'))

	for photo in photos:
		photo_id = photo['id']
		sleep(randint(20,30))
		send_message(peer_id,'photo'+str(owner_id)+'_'+str(photo_id))



if __name__ == '__main__':
	main()
