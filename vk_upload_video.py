#!/usr/bin/python3

import requests
import json
import os
from time import sleep
from glob import glob

v=5.67
token = 'Your Token'
user_id = 415577518
my_folder = "/home/reverse_tcp/Pictures/webm/"


def main():
        files_list = glob(os.path.join(my_folder, '*.webm'))
        for i in range(0, len(files_list)):
                video_name = files_list[i].split('/')[-1]
                r = requests.get('https://api.vk.com/method/video.save?', params={'name': video_name, 'is_private': 1, 'album_id': 104, 'no_comments': 1, 'access_token': token, 'v': v}).json()
                url = r['response']['upload_url']
                with open(files_list[i], 'rb') as file_:
                        try:
                                print(files_list[i])
                                post_sent = requests.post(url, files={'video_file': file_})
                                add_to_playlist = requests.get('https://api.vk.com/method/video.addToAlbum?', params={'album_id': 104, 'owner_id': user_id, 'video_id': post_sent.json()['video_id']  ,'access_token': token, 'v': v})
                        except TimeoutError:
                                print("Connection timed out!")
                        else:
                                print(post_sent.json())

	


if __name__ == '__main__':
        main()
