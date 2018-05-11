import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3306, user="root", password="root", 
	db='car_managing', charset='utf8')

cursor = conn.cursor()
cursor.execute('select * from car')

#row_1 = cursor.fetchone()
#print(row_1)
data = cursor.fetchall()
# print(data)
# print(type(data[0]))
# print(data[0][1])

