# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import os
import re
import time
import urllib.request

main_url = 'https://www.doutula.com/article/list/?page='

headers = {
"User-Agent": 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
}

def down_image(url, name):
	try:
		response = urllib.request.urlopen(url)
		with open(name,'wb') as f:
			f.write(response.read())
	except Exception as e:
		pass

def main():
	n = 1
	for i in range(1, 531):
		wb_data = requests.get(main_url + str(i), headers=headers)
		for article_id in BeautifulSoup(wb_data.text, "lxml").select(".list-group-item"):
			print("Downloading " + article_id["href"])
			wb_data1 = requests.get(article_id["href"], headers=headers)
			for bq_img in BeautifulSoup(wb_data1.text, "lxml").select(".pic-content img"):
				if bq_img["src"][-3:] == 'jpg':
					down_image(bq_img["src"], 'imgs/img' + str(n) + '.jpg')
					n = n + 1
		print("Finish page " + str(i) + "...")
	print("Finish downloads!")

main()