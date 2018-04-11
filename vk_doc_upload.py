#!/usr/bin/python3

import requests
import json
import os
from time import sleep
from glob import glob
from random import randint

v=5.67
token = 'Your token'
user_id = 415577518
chat_const = 2000000000
peer_id = chat_const +  10
my_folder = "/home/reverse_tcp/Pictures/gif/"



def send_message(peer_id, attachment):
	r = requests.get('https://api.vk.com/method/messages.send?', params={'access_token': token,
	 								     'peer_id': peer_id,
	 								     'attachment': attachment,
	 								     'v': v}).json()

def main():
        files_list = sorted(glob(os.path.join(my_folder, '*.gif')))
        for i in range(0, len(files_list)):
                doc_name = files_list[i].split('/')[-1]
                r = requests.get('https://api.vk.com/method/docs.getUploadServer?', params={'access_token': token, 'v': v}).json()
                url = r['response']['upload_url']
                with open(files_list[i], 'rb') as file_:
                        try:
                                print(files_list[i])
                                post_sent = requests.post(url, files={'file': file_})
                                doc_save = requests.get('https://api.vk.com/method/docs.save?', params={'title':doc_name, 'file': post_sent.json()['file']  ,'access_token': token, 'v': v})
                        except TypeError, e:
                                print("Connection timed out!" + str(e))
                        else:
                                try:
                                        doc_id = doc_save.json()['response'][0]['id']
                                        print(doc_id)
                                        sleep(randint(4,10))
                                        send_message(peer_id,'doc'+str(user_id)+'_'+str(doc_id))
                                except KeyError, e:
                                        print 'I got a KeyError - reason "%s"' % str(e)
                                except IndexError, e:
                                        print 'I got an IndexError - reason "%s"' % str(e)
                                


if __name__ == '__main__':
        main()
