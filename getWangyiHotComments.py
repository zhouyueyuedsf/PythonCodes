# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import re

from tkinter import *

song_url = 'http://music.163.com/song?id='
comment_url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_'

headers = {
		"User-Agent": 
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
	}

def deleteUnicodeError(s):
	astral = re.compile(r'([^\u0000-\uffff])')
	newc = ''
	for i, ss in enumerate(re.split(astral, s)):
	    if not i%2:
	        newc += ss
	return newc

def get_hot_comments(song_id):
	param = {'params' : 'XhDhcUHWJvujHDdIwfEJtCfI4b4fN65S76R6rRxX+dehLbkQWiIDN43jBZqt2SmQRv66Y+/buGmKZupY7Hz36gSXyGPKYOFRI9PlnKrzPipTrGg1Ym9d84g1WzkFdcZXsi+BfSti8GBocbBNfxssaEDxgAHtB42ylUtJjEz2a3ifcA6l69NsMoSDgCUaO3uT1atMk0CEf0c7ot/jqIJqTWPPmQC5Y4pcKtuVZI0DzKc=',
			'encSecKey' : 'dbab774326283439c76dfedd666088655877ca6fa4a10d9110ac4a36d308bd2b88b7269cf4ad02ba760d5fe80e1d9485335f2803321fb4f7c5c26505c772dd2a7184b0a6ccaaadbf4e5419e02d923294f612138753cdc972502bc4faa0d3dc742773bbe8b3254edd10779e8e9b6eacb782699c5a38f8f237a535696b972ab34c'}
	url = comment_url + song_id
	web_data = requests.post(url, param)
	data = json.loads(web_data.text)
	hot_comments = data['hotComments']
	total_comments = data['total']
	return hot_comments

def get_song_name(song_id):
	url = song_url + song_id
	web_data = requests.get(url, headers=headers)
	data = BeautifulSoup(web_data.text, "lxml")
	title = data.find_all("em", class_="f-ff2")
	if len(title) == 0:
		return "None"
	else:
		return title[0].string

class WidgetsDemo:
	def __init__(self):
		window = Tk()    
		window.title("获取网易云音乐Top15热评")
		frame2 = Frame(window)
		frame2.pack()
		label = Label(frame2, text = "请输入歌曲ID")
		self.song_id = StringVar()
		entryName = Entry(frame2, textvariable = self.song_id)
		btGetName = Button(frame2, text = "获取热评", command = self.getHotComments)
		label.grid(row = 1, column = 1)
		entryName.grid(row = 1, column = 2)
		btGetName.grid(row = 1, column = 3)
		self.text = Text(window)
		#self.text.configure(state="disabled")
		self.text.pack()
		window.mainloop()

	def getHotComments(self): 
		self.text.delete(0.0, END)
		title = get_song_name(self.song_id.get())
		if title != "None":
			self.text.insert(INSERT, "歌曲名为：" + title + "\n")
			hot_comments = get_hot_comments(self.song_id.get())
			if len(hot_comments) != 0: 
				self.text.insert(INSERT, "共有" + str(len(hot_comments)) + "条热评\n")
				for i in range(len(hot_comments)):
					user_name = hot_comments[i]['user']['nickname']
					likes = hot_comments[i]['likedCount']
					comment = hot_comments[i]['content']
					# print(comment)
					# print(deleteUnicodeError(comment))
					self.text.insert(INSERT, "--------------------------------------------------------------------------------\n")
					self.text.insert(INSERT, "第" + str(i+1) + "条\n")
					self.text.insert(INSERT, "用户昵称：" + user_name + " 点赞数：" + str(likes) + "\n")
					self.text.insert(INSERT, "评论内容：" + deleteUnicodeError(comment) + "\n\n")
			else:
				self.text.insert(INSERT, "对不起，该歌曲暂无热门评论。\n")
		else:
			self.text.insert(INSERT, "对不起，未找到相关歌曲。\n")

WidgetsDemo()