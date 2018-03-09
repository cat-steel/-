import os,requests,re
import mysql.connector

conn = mysql.connector.connect(user='root',password='password',database='test')
cursor = conn.cursor()

cursor.execute('select * from weather')
value = cursor.fetchall()
cursor.close()
conn.close()

def get_url(city):
	url = 'http://www.weather.com.cn/weather1d/'
	for i in value:
		if city == i[0]:
			city_url = url + i[1] + '.shtml#search'
	return city_url
city_url = get_url('广州')
r = requests.get(city_url)
r.encoding = 'utf-8'
response = r.text
we = re.match(r'var hour3data=',response)
print(response)
print(we)