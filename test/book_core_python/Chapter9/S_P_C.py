# -*- coding:utf-8 -*-
# file: S_P_C.py
#
import stackless							# ����stacklessģ��
import Queue								# ����Queueģ��
def Producer(i):							# ����������
	global queue							# ����Ϊȫ��Queue����
	queue.put(i)							# ��������������
	print 'Producer',i, 'add',i
def Consumer():								# ����������
	global queue
	i = queue.get()							# �Ӷ�����ȡ������
	print 'Consumer',i, 'get',i
queue = Queue.Queue()							# ���ɶ��ж���
for i in range(10):
	stackless.tasklet(Producer)(i)					# �������������
for i in range(10):
	stackless.tasklet(Consumer)()					# �������������
stackless.run()								# ִ������

