# -*- coding:utf-8 -*-
# file: PyMySQL.py
#

import MySQLdb											# ����MySQLdbģ��
db = MySQLdb.connect(host='localhost',								# ���ӵ����ݿ⣬������Ϊ����
		user='root',									# �û�Ϊroot
		passwd='python',								# ����Ϊpython
		db='python')									# ���ݿ���Ϊpython
cur = db.cursor()										# ������ݿ��α�
cur.execute('insert into people (name,age,sex) values (\'Jee\',21,\'F\')')			# ִ��SQL���
r = cur.execute('delete from people where age=20')						# ִ��SQL���
r = cur.execute('select * from people')								# ִ��SQL���
con.commit()											# �ύ����
r = cur.fetchall()										# ��ȡ����
print r												# �������
cur.close()											# �ر��α�
db.close()											# �ر����ݿ�����
