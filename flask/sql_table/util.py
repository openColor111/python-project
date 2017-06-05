#!/usr/bin/env python
import pymysql


file_data={}
#获取数据的字典
def update_data():
    conn = pymysql.Connect(host='192.168.128.180',port=3306,user='root',passwd='cisco123',db='test',charset='utf8')
    cursor = conn.cursor()
    sql='select * from uc'
    cursor.execute(sql)

    for line in cursor.fetchall():
        if not line:
            continue
        file_data[line[0]]=line[1]
    conn.close()

#获取table的html
def getable():
    tem_str='<table border=1>'
    tem_str += '<tr><th>user</th><th>age</th><th>operation</th></tr>'
    tem_str += '<tr>'
    for i,j in file_data.items():
    #拼接html代码，%(变量)进行格式化
        tem_str += "<td>%s</td><td>%s</td><td><a href=/delete?user=%s>delete</a></td>"%(i,j,i)
        tem_str += "</tr>"
    return tem_str

def add_form_htm():
    return '''
            <form action="add">
            user: <input type="text" name="user">
            age: <input type="text" name="age">
            <input type="submit" name="提交">
            </form>
    
    '''
def update_file(user,age):
    conn = pymysql.Connect(host='192.168.128.180',port=3306,user='root',passwd='cisco123',db='test',charset='utf8')
    cursor = conn.cursor()
    sql = 'insert into uc values("%s",%s)'%(user,age)
    cursor.execute(sql)

def get_all_html():
    return add_form_htm()+getable()

def dele(user):
    conn = pymysql.Connect(host='192.168.128.180',port=3306,user='root',passwd='cisco123',db='test',charset='utf8')
    cursor = conn.cursor()
    sql='delete from uc where user="%s"'%(user)
    cursor.execute(sql)
