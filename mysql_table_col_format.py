#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
功能：数据库范式化

流程：
1.选择范式化对象列
2.生成不重复项列表
3.建新表
	3.1	表名-选择列字段名
	3.2	字段名-选择列字段名
	3.3	插入不重复项列表
	3.4	生成索引列
4.数据表范式化
	4.1	选择列
	4.2	根据新表的索引替换原有内容
'''

import pymysql
'''
db_centos  
host='192.168.200.99',user='root',passwd='Xumy8!75',db='vmware',port=3306,charset='utf8'
db_hostpark=
host='47.89.48.123',user='seacsuto_xmy',passwd='xumy8175',db='seacsuto_vmware',port=3306,charset='utf8'
'''
# 打开数据库连接

db = pymysql.connect(host='47.89.48.123',user='seacsuto_xmy',passwd='xumy8175',db='seacsuto_vmware',port=3306,charset='utf8')  

_table='sku_201703'
_col_name='Platform Group'

cursor=db.cursor()
sql='select `'\
	+_col_name+'` from '\
	+_table\
	+' group by `'+_col_name+'`'
print(sql,'\n',_col_name)

cursor.execute(sql)
data=cursor.fetchall()
for row in data:
	print(row[0])



