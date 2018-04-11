#!/usr/bin/python3
import sys
import os
import requests
import json
from glob import glob
from time import sleep
from random import randint



access_token = 'Your token'
user_id = 415577518
album_id = 245535621
try:
	my_folder = "/run/media/reverse_tcp/b71fb0a4-d495-4012-b108-5fd3d64cbd00/home/alarm/" + str(sys.argv[1])
except:
	print("No folder, give me argument")
v =5.63

def write_json(data, filename):
	with open(filename, 'w') as file:
		json.dump(data,filename, indent=2, ensure_ascii=False)


def get_upload_server():
	r = requests.get('https://api.vk.com/method/photos.getUploadServer?', params={'access_token': access_token,
										      'album_id': album_id,	
											'v': v}).json()
	return r['response']['upload_url']





def main():
	upload_url = get_upload_server()
	files_list = glob(os.path.join(my_folder, '*'))
	for a_file in sorted(files_list):
		#sleep(randint(1,3))
		file = {'file1': open(a_file, 'r')}
		ur = requests.post(upload_url, files=file).json()
		r = requests.get('https://api.vk.com/method/photos.save?' ,params={'access_token': access_token,
									   'album_id': ur['aid'],
								       	   'server': ur['server'],
									   'hash': ur['hash'],
									   'photos_list': ur['photos_list'],
									   'v': v}).json()
		print(a_file)
		print(r)

if __name__ == '__main__':
	main()
