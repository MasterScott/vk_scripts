#!/usr/bin/python3

import requests
import json
from time import sleep


access_token = 'Your Token' #https://goo.gl/r0zGiF
group_id = '-145607642' #айди группы с минусом -1234565
v = 5.63




def write_json(data, filename):
	with open(filename, 'w') as file:
		json.dump(data, file, indent=2,ensure_ascii=False)



def delete_comment(comment_id):
	r = requests.get('https://api.vk.com/method/wall.deleteComment?', params={'access_token': access_token,'owner_id': group_id, 'comment_id': comment_id, 'v': v}).json()


def get_comments(post_id):
	offset = 0
	number_of_comments = requests.get('https://api.vk.com/method/wall.getComments?', params={'access_token': access_token,'owner_id': group_id,'count': 100, 'offset':0, 'post_id': post_id, 'v': v}).json()['response']['count']
	
	while True:
		r = requests.get('https://api.vk.com/method/wall.getComments?', params={'access_token': access_token,'owner_id': group_id,'count': 100, 'offset':0, 'post_id': post_id, 'v': v}).json()
		comments_id = []
		try:
			comments = r['response']['items']
			for comment in comments:
				comments_id.append(comment)

		except:
			print("No comments in post")
		if number_of_comments < offset:  
			break
		offset +=100

	return comments_id

def get_posts_id():
	offset = 0
	all_id = []
	number_of_posts = requests.get('https://api.vk.com/method/wall.get?', params={'owner_id': group_id, 'count': 1, 'offset': 0, 'v': v}).json()['response']['count']
	while True:
		r = requests.get('https://api.vk.com/method/wall.get?', params={'owner_id': group_id, 'count': 100, 'offset': offset, 'v': v}).json()

		
		posts = r['response']['items']
		for post in posts:
			all_id.append(post['id'])

		#last_post_date = posts[-1]['date']

		#if (last_post_date < date_x):
		if number_of_posts < offset:  
			break
		offset +=100
	return all_id


def main():
# (*)получить все посты
# (*)извлечь id из поста
# (*)найти комментарии по id поста
# (*)если ссылка, фото или ключевое слово, удалить пост
# 

	# while True:
	# 	sleep(1)

	not_allowed = {'http://', 'https://', 'реклама'}

	print(get_posts_id())
	for post_id in get_posts_id():
		comments_array = get_comments(post_id)
		for comment in comments_array:
			isDelete = False
			try:
				for attach in comment['attachments']:
					if (attach['type'] == 'photo'):
						delete_comment(comment['id'])
						print("Photo deleted!")
						isDelete = True
						break
			except:
				print("No attachments in comment")

			if not isDelete:
				if any(not_allowed):
					for element in not_allowed:
						if element in comment['text']:
							delete_comment(comment['id'])
							print("Comment deleted!")
							break



if __name__ == '__main__':
	main()


	#Делаешь тестовую группу, создаешь посты и комменты.
	#Получаешь токен https://goo.gl/r0zGiF
	#Вставляешь токен и id группы
	#Запускаешь скрипт в терминале (python3 vk_purge_comments.py)
	#скрипт отработает, комменты чисты
