#!/usr/bin/python3
import os
import requests
import json
from time import sleep
from pathlib import Path 

token = 'Your token'
v=5.52

def setup_download_dir():
	download_dir = Path('Photos')
	if not download_dir.exists():
		download_dir.mkdir()
	return download_dir


def write_json(data):
	with open('photos.json', 'w') as file:
		json.dump(data, file, indent= 2, ensure_ascii=False)


def get_largest(size_dict):
	if size_dict['width'] >= size_dict['height']:
		return size_dict['width']
	else:
		return size_dict['height']

def download_photo(url):
	r = requests.get(url, stream=True)
	filename = url.split('/')[-1]
	with open("Photos/"+filename, 'bw') as file:
		for chunk in r.iter_content(4096):
			file.write(chunk)


def main():
	offset = 0
	all_photos = []

	
	while True:
		sleep(1)
		r = requests.get('https://api.vk.com/method/photos.get?', params={'owner_id': 415577518,
	 																  'access_token': token, 
	 															   	  'album_id': 'saved',
	 															   	  'photo_sizes': True,
	 										 						  'count': 100,
	 										  						  'offset': offset})
		photos = r.json()['response']
		all_photos.extend(photos)
		# count = all_photos['count']

		print(offset)

		if offset >= 1306:
			break

		offset+=100
		

	write_json(all_photos)
	photos = json.load(open('photos.json'))

	setup_download_dir()

	for photo in photos:
		sizes = photo['sizes']

		max_size_url = max(sizes, key = get_largest)['src']
		download_photo(max_size_url)




if __name__ == '__main__':
	main()
