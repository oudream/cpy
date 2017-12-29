# -*- coding:utf-8 -*-
# file: ADO.py
#
import win32com.client								# ����win32com.client
adoCon = win32com.client.Dispatch('ADODB.Connection')				# �������Ӷ���
adoCon.Open('podbc')  								# ���ӵ�����Դ
adoRS = win32com.client.Dispatch('ADODB.Recordset')				# ����Recordset����
adoRS.Open('[' + 'people' + ']', adoCon, 1, 3)					# ������Դ�е�people��
adoRS.MoveFirst()								# �ƶ�����һ����¼
for i in range(adoRS.RecordCount):
	print adoRS.Fields('name').Value					# �����¼��name
	print adoRS.Fields('age').Value						# �����¼��age
	print adoRS.Fields('sex').Value						# �����¼��sex
	adoRS.MoveNext()
adoRS.AddNew()									# ����¼�¼
adoRS.Fields('name').Value = 'Kate'						# �¼�¼��name
adoRS.Fields('age').Value = 22							# �¼�¼��age
adoRS.Fields('sex').Value = 'Female'						# �¼�¼��sex
adoRS.Update()									# ���¼�¼
adoRS.Close()									# �رձ�
adoCon.Close()									# �ر����ݿ�����
