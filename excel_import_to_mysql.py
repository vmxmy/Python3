#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
流程：
1.读取excel
2.连接数据库
3.根据excel名称创建表table
4.插入数据
5.断开连接
'''

import xlrd
import pymysql
 
#设置基本变量
'''
db_centos  
host='192.168.200.99',user='root',passwd='Xumy8!75',db='vmware',port=3306,charset='utf8'
db_hostpark=
host='47.89.48.123',user='seacsuto_xmy',passwd='xumy8175',db='seacsuto_vmware',port=3306,charset='utf8'
'''
#Mysql主机设置
_host = '47.89.48.123'
_db = 'seacsuto_vmware'
_user = 'seacsuto_xmy'
_password = 'xumy8175'

#新建表名
_table = 'product_tree_201703'

#Excel文件设置
_excel_path='/Users/xumingyang/Downloads/'
_excel_name ='product_tree.xlsx'
_file_name=_excel_path+_excel_name
_sheet_title_row=1
excel = xlrd.open_workbook(_file_name)
_sheet = excel.sheet_by_index(0)
print(_excel_name)
 
#读取excel


rows = _sheet.nrows
cols = _sheet.ncols
print("行数=",rows,"列数=",cols)

data = []
fields=''
#创建好要数据,如果第一行是表头的话，从1开始，若第一行就是数据，从0开始
#在这里有必要提醒大家的是,这只是个简单的数据处理,如果你的数据有一些特殊的字符,或者数据,需要先将数据处理好了之后再来打包导入
for i in range(_sheet_title_row,rows):
  data.append(_sheet.row_values(i))
#print(data)
for i in range(0,cols):
    fields = fields+'%s,'

#取得表头字段 和 表第1行 内容
col_names=_sheet.row_values(_sheet_title_row-1)
col_value=_sheet.row_values(_sheet_title_row)
#print("表头=",col_names)

#连接数据库
conn = pymysql.connect(host='47.89.48.123',user='seacsuto_xmy',passwd='xumy8175',db='seacsuto_vmware',port=3306,charset='utf8')
cursor = conn.cursor()

#创建表
sql = 'create table '\
	+_table+' (' \
	#+'id int NOT NULL AUTO_INCREMENT PRIMARY KEY, ' \
	
 
for i in range(0, cols):
	col_type=isinstance(col_value[i],float)
	
	#设置字段类型
	if col_type== True:
		col_type=' float'
	else:
		col_type=' varchar(1024)'

	sql = sql + '`'+col_names[i] +'`'+ col_type
	if i != cols-1:
		sql += ','
sql = sql + ') ENGINE=InnoDB DEFAULT CHARSET=utf8'
print(sql)

cursor.execute(sql)

#导入数据
sql='insert into '\
	+_table\
	+' values('\
	+fields[:-1]\
	+')' 
#print(sql)
cursor.executemany(sql,data)

sql='ALTER TABLE '\
	+_table\
	+' add id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY first'
cursor.execute(sql)
conn.commit()

