# -*- coding:utf-8 -*-
# file: ODBC.py
#
import odbc										# ����odbcģ��
con = odbc.odbc('podbc')								# ���ӵ����ݿ⣬��������Դ������д������
cursor = con.cursor()									# ����cursor����
cursor.execute('select id,name from people where id = 1')				# ִ��SQL����ѯIDΪ1�ļ�¼
r = cursor.fetchall()									# ������м�¼
print r											# �����¼
cursor.execute('insert into people (name,age,sex) values (\'Jee\',21,\'female\')')	# ��Ӽ�¼
cursor.execute('DELETE FROM people where id = 3')					# ɾ��IDΪ3�ļ�¼
con.commit()										# �ύ����
cursor.close()										# �ر�cursor
con.close()										# �ر�����
