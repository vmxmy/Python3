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
			`Platform Group` REGEXP 'Horizon'	# 产品组
		and
			`Product Family` REGEXP 'Horizon'	# 产品类别_pl
	"""
#print(sql)
cursor.execute(sql)
data=cursor.fetchall()

#输出结果
print('sku','\t','listprice','\t','product')
for row in data:
	sku=row[6]
	listprice=row[8]
	product=row[4]
	print('%s\t¥ %.0f\t%s' % (sku,listprice,product))
	print('------------------------------------------\n')
	'''
	#根据产品sku计算服务sku
	service_sku='^'+row[6][0:len(row[6])-2]+'-'+'[^-]*'+'-SSS'+row[6][len(row[6])-2:len(row[6])]+'$'
	#print(service_sku)
	sql='select * from '+_table +' where `Part Number` REGEXP '+'\''+service_sku+'\''+'group by `Part Number`'
	#print(sql)
	cursor.execute(sql)
	data_s=cursor.fetchall()
	for row_s in data_s:
		print('%s\t¥%.0f\t%s\n' % (row_s[6],row_s[8],row_s[4]))
	print('=====================================================================')
	'''
db.close()