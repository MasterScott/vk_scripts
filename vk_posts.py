#!/usr/bin/python3
import requests
import json
from datetime import datetime
from time import sleep
import csv

def write_json(data):
		with open('posts.json', 'w') as file:
			json.dump(data, file, indent=2, ensure_ascii=False)


def to_json(past_dict):
	try:
		data = json.load(open('posts_data.json'))
	except:
		data = []

	data.append(post_dict)

	with open('posts_data.json', 'w') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)


def write_csv(data):
	with open('post_data.csv', 'a') as file:
		writer = csv.writer(file)

		writer.writerow((data['likes'],
						 data['reposts'],
						 data['text']
						 ))


def get_data(post):
	try:
		post_id = post['id']
	except:
		post_id = 0

	try:
		likes = post['likes']['count']
	except:
		likes = 'zero'

	try:
		reposts = post['reposts']['count']
	except:
		reposts = 'zero'

	try:
		text = post['text']
	except:
		text = '***'

	data = {
		'id': post_id,
		'likes': likes,
		'reposts': reposts,
		'text': text
	}

	return data


def main():
	start = datetime.now()
	#https://api.vk.com/method/wall.get?user_id=210700286&v=5.52

	group_id = '-30666517'
	offset = 0
	date_x = 1456978229
	all_posts = []

	while True:
		sleep(1)
		r = requests.get('https://api.vk.com/method/wall.get?', params={'owner_id': group_id, 'count': 100, 'offset': offset})
		posts = r.json()['response']
		print(posts)
		all_posts.extend(posts)
		print(all_posts)

		oldest_post_date = posts[-1]['date']

		offset += 100
		print(offset)

		if (oldest_post_date < date_x):
			break

		data_posts = []

		for post in all_posts:
			post_data = get_data(post)
			write_csv(post_data)

		end = datetime.now()

		total = end - start
		print(len(all_posts))
		print(str(total))






	#write_json(r.json())

	#data = json.load(open('posts.json'))
	#print(len(data['response']))



if __name__ == '__main__':
	main()