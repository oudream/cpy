# -*- coding:utf-8 -*-
# file: DAO.py
#
import win32com.client								# ����win32com.client
dbEngine = win32com.client.Dispatch('DAO.DBEngine.35')				# ����COM����
daoDB = dbEngine.OpenDatabase('python.mdb')					# �����ݿ�
daoRS = daoDB.OpenRecordset('people')						# �򿪱�
daoRS.MoveLast()     								# �ƶ������һ����¼
print daoRS.RecordCount								# �����¼����
print daoRS.Fields('name').Value						# ������һ����¼��name
print daoRS.Fields('age').Value							# ������һ����¼��age
print daoRS.Fields('sex').Value							# ������һ����¼��sex
daoRS.AddNew()									# ����¼�¼
daoRS.Fields('name').Value = 'Kate'						# �¼�¼��name
daoRS.Fields('age').Value = 22							# �¼�¼��age
daoRS.Fields('sex').Value = 'Female'						# �¼�¼��sex
daoRS.Update()									# ���¼�¼
daoRS.Close()									# �رձ�
daoDB.Close()									# �ر����ݿ�����
