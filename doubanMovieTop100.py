from bs4 import BeautifulSoup
import requests
import re
import time
import csv
# coding=utf-8

headers = {
"User-Agent": 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
}

urls = ["https://movie.douban.com/top250?start={}".format(str(i)) for i in range (0,50,25)]

movie_info = []

def get_url_movie(url):
	wb_data = requests.get(url, headers=headers)
	soup = BeautifulSoup(wb_data.text, "lxml")
	movie_hrefs = soup.select(".info .hd a")
	for movie_href in movie_hrefs:
		get_movie_info(movie_href['href'])
		#time.sleep(1)

def get_movie_info(url):
	print("I am getting info from " + url)
	wb_data = requests.get(url, headers=headers)
	soup = BeautifulSoup(wb_data.text, "lxml")
	names = soup.select("#content h1 span")
	if len(names) == 0:
		data = {
		"name": "Not found",
		"director": "Not found",
		"score": "Not found",
		"country": "Not found"
		}
		print(data)
		movie_info.append(data)
		print("I am done!")
		return
	directors = soup.select("#info span .attrs a")
	if len(directors) == 0:
		return
	country = re.findall('<span class="pl">制片国家/地区:</span>(.*?)<br/>', wb_data.text, re.S)
	if len(country) == 0:
		return
	scores = soup.select(".rating_self strong")
	if len(scores) == 0:
		return
	data = {
		"name": names[0].get_text(),
		"director": directors[0].get_text(),
		"score": scores[0].get_text(),
		"country": country[0].split(" ")[1]
	}
	print(data)
	movie_info.append(data)
	print("I am done!")

# for url in urls:
# 	get_url_movie(url)

# print(movie_info)

# movie_info = [{'country': '美国', 'director': '弗兰克·德拉邦特', 'name': '肖申克的救赎 The Shawshank Redemption', 'score': '9.6'}, {'country': '中国大陆', 'director': '陈凯歌', 'name': '霸王别姬', 'score': '9.5'}, {'country': '法国', 'director': '吕克·贝松', 'name': '这个杀手不太冷 Léon', 'score': '9.4'}, {'country': '美国', 'director': '罗伯特·泽米吉斯', 'name': '阿甘正传 Forrest Gump', 'score': '9.4'}, {'country': '意大利', 'director': '罗伯托·贝尼尼', 'name': '美丽人生 La vita è bella', 'score': '9.5'}, {'country': '日本', 'director': '宫崎骏', 'name': '千与千寻 千と千尋の神隠し', 'score': '9.2'}, {'country': '美国', 'director': '史蒂文·斯皮尔伯格', 'name': "辛德勒的名单 Schindler's List", 'score': '9.4'}, {'country': '美国', 'director': '詹姆斯·卡梅隆', 'name': '泰坦尼克号 Titanic', 'score': '9.2'}, {'country': '美国', 'director': '克里斯托弗·诺兰', 'name': '盗梦空间 Inception', 'score': '9.2'}, {'country': '美国', 'director': '安德鲁·斯坦顿', 'name': '机器人总动员 WALL·E', 'score': '9.3'}, {'country': '意大利', 'director': '朱塞佩·托纳多雷', 'name': "海上钢琴师 La leggenda del pianista sull'oceano", 'score': '9.2'}, {'country': '印度', 'director': '拉吉库马尔·希拉尼', 'name': '三傻大闹宝莱坞 3 Idiots', 'score': '9.1'}, {'country': '美国', 'director': '拉斯·霍尔斯道姆', 'name': "忠犬八公的故事 Hachi: A Dog's Tale", 'score': '9.2'}, {'country': '法国', 'director': '克里斯托夫·巴拉蒂', 'name': '放牛班的春天 Les choristes', 'score': '9.2'}, {'country': '香港', 'director': '刘镇伟', 'name': '大话西游之大圣娶亲 西遊記大結局之仙履奇緣', 'score': '9.2'}, {'country': '日本', 'director': '宫崎骏', 'name': '龙猫 となりのトトロ', 'score': '9.1'}, {'country': '美国', 'director': '弗朗西斯·福特·科波拉', 'name': '教父 The Godfather', 'score': '9.2'}, {'country': '美国', 'director': '彼得·威尔', 'name': '楚门的世界 The Truman Show', 'score': '9.1'}, {'country': '美国', 'director': '维克多·弗莱明', 'name': '乱世佳人 Gone with the Wind', 'score': '9.2'}, {'country': '意大利', 'director': '朱塞佩·托纳多雷', 'name': '天堂电影院 Nuovo Cinema Paradiso', 'score': '9.1'}, {'country': '法国', 'director': '奥利维埃·纳卡什', 'name': '触不可及 Intouchables', 'score': '9.1'}, {'country': '美国', 'director': '加布里埃莱·穆奇诺', 'name': '当幸福来敲门 The Pursuit of Happyness', 'score': '8.9'}, {'country': 'Not found', 'director': 'Not found', 'name': 'Not found', 'score': 'Not found'}, {'country': 'Not found', 'director': 'Not found', 'name': 'Not found', 'score': 'Not found'}, {'country': '香港', 'director': '刘伟强', 'name': '无间道 無間道', 'score': '9.0'}, {'country': '美国', 'director': '西德尼·吕美特', 'name': '十二怒汉 12 Angry Men', 'score': '9.4'}, {'country': '美国', 'director': '罗伯·莱纳', 'name': '怦然心动 Flipped', 'score': '8.9'}, {'country': '美国', 'director': '彼得·杰克逊', 'name': '指环王3：王者无敌 The Lord of the Rings: The Return of the King', 'score': '9.1'}, {'country': '美国', 'director': '克里斯托弗·诺兰', 'name': '星际穿越 Interstellar', 'score': '9.1'}, {'country': '美国', 'director': '李安', 'name': '少年派的奇幻漂流 Life of Pi', 'score': '9.0'}, {'country': '日本', 'director': '宫崎骏', 'name': '天空之城 天空の城ラピュタ', 'score': '9.0'}, {'country': '美国', 'director': '威廉·惠勒', 'name': '罗马假日 Roman Holiday', 'score': '8.9'}, {'country': '中国大陆', 'director': '姜文', 'name': '鬼子来了', 'score': '9.2'}, {'country': '美国', 'director': '克里斯托弗·诺兰', 'name': '蝙蝠侠：黑暗骑士 The Dark Knight', 'score': '9.0'}, {'country': '香港', 'director': '刘镇伟', 'name': '大话西游之月光宝盒 西遊記第壹佰零壹回之月光寶盒', 'score': '8.9'}, {'country': '中国大陆', 'director': '张艺谋', 'name': '活着', 'score': '9.1'}, {'country': '英国', 'director': '盖·里奇', 'name': '两杆大烟枪 Lock, Stock and Two Smoking Barrels', 'score': '9.0'}, {'country': '美国', 'director': '彼特·道格特', 'name': '飞屋环游记 Up', 'score': '8.9'}, {'country': '德国', 'director': '弗洛里安·亨克尔·冯·多纳斯马尔克', 'name': '窃听风暴 Das Leben der Anderen', 'score': '9.1'}, {'country': '美国', 'director': '米洛斯·福尔曼', 'name': "飞越疯人院 One Flew Over the Cuckoo's Nest", 'score': '9.0'}, {'country': '美国', 'director': '路易·西霍尤斯', 'name': '海豚湾 The Cove', 'score': '9.3'}, {'country': '美国', 'director': '马丁·布莱斯', 'name': '闻香识女人 Scent of a Woman', 'score': '8.9'}, {'country': '美国', 'director': '詹姆斯·麦克特格', 'name': 'V字仇杀队 V for Vendetta', 'score': '8.8'}, {'country': '日本', 'director': '宫崎骏', 'name': '哈尔的移动城堡 ハウルの動く城', 'score': '8.9'}, {'country': '美国', 'director': '弗朗西斯·福特·科波拉', 'name': '教父2 The Godfather: Part Ⅱ', 'score': '9.1'}, {'country': '美国', 'director': '朗·霍华德', 'name': '美丽心灵 A Beautiful Mind', 'score': '8.9'}, {'country': '美国', 'director': '彼得·杰克逊', 'name': '指环王2：双塔奇兵 The Lord of the Rings: The Two Towers', 'score': '8.9'}, {'country': '新西兰', 'director': '彼得·杰克逊', 'name': '指环王1：魔戒再现 The Lord of the Rings: The Fellowship of the Ring', 'score': '8.9'}, {'country': '美国', 'director': '彼得·威尔', 'name': '死亡诗社 Dead Poets Society', 'score': '8.9'}, {'country': '日本', 'director': '岩井俊二', 'name': '情书 Love Letter', 'score': '8.8'}]
csvFile = open('doubanMovieTop100.csv', newline='')
writer = csv.writer(csvFile)
writer.writerow(["Name", "Director", "Country", "Score"])
for i in range(len(movie_info)):
    writer.writerow([movie_info[i]["name"], movie_info[i]["director"], movie_info[i]["country"], movie_info[i]["score"]])
csvFile.close()