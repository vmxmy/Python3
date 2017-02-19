#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
'''
db_centos  
host='192.168.200.99',user='root',passwd='Xumy8!75',db='vmware',port=3306,charset='utf8'
db_hostpark=
host='47.89.48.123',user='seacsuto_xmy',passwd='xumy8175',db='seacsuto_vmware',port=3306,charset='utf8'
'''
# 打开数据库连接

db = pymysql.connect(host='47.89.48.123',user='seacsuto_xmy',passwd='xumy8175',db='seacsuto_vmware',port=3306,charset='utf8')  
cursor=db.cursor()
_table='sku_201703'

#从数据库里按条件搜索记录
sql='SELECT * FROM '+_table\
	+r"""
		WHERE 
			`Part Number` REGEXP 'C\$' #C结尾
		and
			`Part Number` not REGEXP 'SSS'  #no SSS
		and 
			`Part Number` not REGEXP 'UG'   #no UG
		and
			`Platform Group` REGEXP '.*'	# 产品组
		and
			`Product Family` REGEXP '.*'	# 产品类别_pl
		group by `Part Number`
	"""
#print(sql)
cursor.execute(sql)
data=cursor.fetchall()

for row in data:
	sku=row[1]
	product=row[4]
	print(sku,'\n',product)
