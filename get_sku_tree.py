#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
功能：取得数据库树结构

流程：
1.设置级数对应字段名
2.选择：
	2.1 显示级数
	2.2	显示节点
		2.2.1 如指明则显示指定至节点及其所有子节点
		2.2.2 未指明则遍历所有节点
3.
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

#根据 表名 取得所有字段名
def get_field_name(_table_name):
	cursor=db.cursor()
	sql='SELECT  COLUMN_NAME FROM information_schema.`COLUMNS` where TABLE_NAME like \''+_table_name+'\''
	print(sql)
	cursor.execute(sql)
	data=cursor.fetchall()
	db.commit()
	return data

#设置 深度 对应的字段
tree_node_name=[]
_field_index=[2,3,4,5]
_table_name='sku_201703'

data=get_field_name(_table_name)

for i in _field_index:
	tree_node_name.append(data[i-1][0])
print(tree_node_name)

#给树节点赋值
#def 

#根据 起始深度，显示深度显示树
_start_level=1	#起始的父节点深度
_start_index=1	#父节点索引
_show_level=2	#遍历的深度

def tree_show_children(table_name,tree_node_name,parent_level,parent_index):
	cursor=db.cursor()
	parent_field=tree_node_name[parent_level-1]
	children_field=tree_node_name[parent_level]
	parent_name='HORIZON'
	print('\n父节点：%s\n子节点：%s\n父节点关键字：%s\n' % (parent_field,children_field,parent_name))

	sql='select * from `'+table_name +'` where `'+parent_field+'` REGEXP \''+parent_name+'\''\
		+r"""
		and
			`Part Number` REGEXP 'C\$' #C结尾
		and
			`Part Number` not REGEXP 'SSS'  #no SSS
		and 
			`Part Number` not REGEXP 'UG'   #no UG
		"""\
		+'group by `'+children_field+'`'
	print(sql)
	cursor.execute(sql)
	data=cursor.fetchall()
	return data

data=tree_show_children(_table_name,tree_node_name,_start_level,1)
counter=0
for row in data:
	counter+=1
	print(counter)
	for i in [_start_level,_start_level+1]:
			print(row[i])
	print('\n')

	