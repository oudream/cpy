# -*- coding:utf-8 -*-
# file: addmessage.py
#
import cgi
import sqlite3											# ����sqlite3ģ��
import datetime
print
print 'Status: 200 OK'
print 'Content-type: text/html'
print
form = cgi.FieldStorage()
name = unicode(form["name"].value, 'GBK')
mail = unicode(form["email"].value, 'GBK')
site = unicode( form["site"].value, 'GBK')
content = unicode(form["content"].value, 'GBK')
now = datetime.datetime.now()
time = now.strftime('%Y-%m-%d %H:%M:%S')
con = sqlite3.connect('message')									# ���ӵ����ݿ�
cur = con.cursor()										# ������ݿ��α�
cur.execute("INSERT INTO message VALUES(?,?,?,?,?)", (name, mail, site, content, time))
con.commit()
# ִ��SQL���
cur.close()											# �ر��α�
con.close()
print '''
<html>
<head>
<title>��ӳɹ�</title>
</head>
<body>
<h1>��ӳɹ�</h1>
<br>
<a href=show.py>����鿴����</a>
</body>
</html>
'''
