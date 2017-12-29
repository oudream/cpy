# -*- coding:utf-8 -*-
# file: threaddaemon.py
# 
import threading							# ����threadingģ��
import time								# ����timeģ��
class mythread(threading.Thread):					# ͨ���̳д�����
	def __init__(self,threadname):					# ��ʼ������
		threading.Thread.__init__(self,name = threadname)	# ���ø���ĳ�ʼ������
	def run(self):							# ����run����
		time.sleep(5)						# ����timeģ���е�sleep���������߳�����5��	
		print self.getName()
def func1():								# ���庯��func1
	t1.start()						
	print 'func1 done'
def func2():								# ���庯��func2
	t2.start()
	print 'func2 done'
t1 = mythread('t1')							# ��ʵ����
t2 = mythread('t2')							# ��ʵ����
t2.setDaemon(True)							# ����t2��Daemon��־
func1()									# ���ú���func1
func2()									# ���ú���func2

