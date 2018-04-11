#!/usr/bin/python3

import requests
import json
from bs4 import BeautifulSoup

token = 'Your token'
owner_id = 415577518
v = 5.63




def write_json(data, filename):
	with open(filename, 'w') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)


def download_file(url):
	r = requests.get(url, stream=True)

	filename = url.split('/')[-1]

	with open(filename, 'bw') as file:
		for chunk in r.iter_content(1024000):
			file.write(chunk)



def parse_playlist():
	return requests.get('https://api.vk.com/method/video.getAlbums?', params={'owner_id': owner_id, 'need_system': True,'count': 100, 'access_token': token, 'v': v})



def parse_videos(album_id):
	return requests.get('https://api.vk.com/method/video.get?', params={'owner_id': owner_id, 'album_id': album_id, 'count': 1, 'access_token': token, 'v': v})



def get_url(url):
	html = requests.get(url).text
	soup = BeautifulSoup(html, 'lxml')

	video_url = soup.find('div', id='page_wrap').find('source').get('src').split('?')[0]
	download_file(video_url)



def main():

	playlist = parse_playlist()
	write_json(playlist.json()['response'], 'video_playlists.json')

	videos = parse_videos(-2).json()['response']['items']
	write_json(videos, 'videos.json')

	for video in videos:
		if 'vk.com' in video['player']:
			url = video['player']
			get_url(url)


if __name__ == '__main__':
	main()
