# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import os
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import numpy as np

song_list_url = 'http://music.163.com/playlist?id=377841230'

headers = {
"User-Agent": 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
}

song_name_list = []
song_url_list = []
song_lyric_list = []

def get_url_song(url):
	wb_data = requests.get(url, headers=headers)
	soup = BeautifulSoup(wb_data.text, "lxml")
	song_ids = soup.select(".f-hide a")
	for song_id in song_ids:
		song_name_list.append(song_id.text)
		song_url_list.append(song_id["href"][9:])
		get_song_lyric(song_id.text, song_id["href"][9:])
		#time.sleep(1)
	print("I am done!")

def get_song_lyric(name, id):
	print("Start to get lyric of song " + id)
	lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(id) + '&lv=1&kv=1&tv=-1'
	lyric = requests.get(lrc_url)
	json_obj = lyric.text
	j = json.loads(json_obj)
	lrc = j['lrc']['lyric']
	pat = re.compile(r'\[.*\]')
	lrc = re.sub(pat, "", lrc)
	lrc = lrc.strip()
	lrc = lrc.replace("作曲", "").replace("作词", "").replace("编曲", "").replace("制作", "").replace("女声", "").replace("录音", "").replace("吉他", "")
	lrc = lrc.replace("music", "").replace("：", "").replace("“","").replace("”","").replace("‘","").replace("’","").replace(" ", "")
	lrc = lrc.replace("\"", "").replace(":", "").replace("\'", "").replace("/", "").replace("\\", "").replace("\n", "").replace(" ", "")
	song_lyric_list.append(lrc)
	#print(lrc)

get_url_song(song_list_url)
print(song_lyric_list)

# 拼接字符串
text = "".join(song_lyric_list)

# jieba分词
wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)

#print(wl_space_split)

# my_wordcloud = WordCloud(background_color="white", max_words=6000, 
#                          max_font_size=40, random_state=42,
#                          font_path='C:\Windows\Fonts\AdobeHeitiStd-Regular.otf').generate(wl_space_split)

# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()



d = os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join(d, "wangyiyun.jpg")))
my_wordcloud = WordCloud(background_color="white", max_words=4000, mask=alice_coloring,
                         max_font_size=60, random_state=42,
                         font_path='C:\Windows\Fonts\AdobeHeitiStd-Regular.otf').generate(wl_space_split)

image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

my_wordcloud.to_file(os.path.join(d, "wechat_cloud6.png"))