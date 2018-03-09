import os
import mysql.connector

conn = mysql.connector.connect(user='root',password='password',database='test')
cursor = conn.cursor()

fp = open(r'D:\person\learn\py\weather\tianqi.txt')
fv = fp.readlines()
fp.close()

for i in fv:
	b = i.strip(' \n\n\t\r')
	a = b.split('=')
	try:
		cursor.execute('insert into weather (city,code) values (%s,%s)',(a[1],a[0]))
	except:
		print('空格')
	print(a[0])
conn.commit()
cursor.close()
conn.close()
