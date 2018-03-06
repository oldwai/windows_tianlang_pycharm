#coding:utf-8
"""
# filename  conn.py
import MySQLdb
try:              # 尝试连接数据库
    conn = MySQLdb.connect("localhost","root","123456","mysql",charset="utf8")  # 定义连接数据库的信息
except MySQLdb.OperationalError, message:  # 连接失败提示
    print "link error"

cursor=conn.cursor()          #定义连接对象
cursor.execute("select * from user")  #使用cursor提供的方法来执行查询语句
data=cursor.fetchall()         #使用fetchall方法返回所有查询结果
print data              #打印查询结果
cursor.close()            #关闭cursor对象
conn.close()
"""




