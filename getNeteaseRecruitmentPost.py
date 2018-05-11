# -*- coding:utf-8 -*-
import requests
import json

headers = {
		"User-Agent": 
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
	}

city = {"北京": "1", "上海": "2", "广州": "138", "杭州": "229"}

work_type_url = 'http://campus.163.com/getPostType.do'
work_position_url = 'http://campus.163.com/position/queryList.do?'

def get_work_type():
	web_data = requests.get(work_type_url, headers=headers)
	data = json.loads(web_data.text)["data"]
	work_type = {}
	for d in data:
		work_type[d["value"]] = d["option"]
	return work_type

def get_positions(type='', city=''):
	page_data = requests.get(work_position_url + "type=" + type + "&cityId=" + city, headers=headers)
	total_pages = json.loads(page_data.text)["data"]["page"]["totalPages"]
	positions = []
	for i in range(total_pages):
		web_data = requests.get(work_position_url + "type=" + type + "&cityId=" + city + "&pageNumber=" + str(i+1), headers=headers)
		position_data = json.loads(web_data.text)["data"]["list"]
		#print(position_data)
		for p in position_data:
			positions.append((p["id"], p["name"], p["typeName"], p["cityName"]))
	return positions

type = get_work_type()
positions = get_positions(city=city["杭州"])
print(positions)
print(len(positions))