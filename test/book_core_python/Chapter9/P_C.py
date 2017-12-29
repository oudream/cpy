# -*- coding:utf-8 -*-
# file: P_C.py
#
import threading							# ����threadingģ��
class Producer(threading.Thread):					# ������������
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global x
		con.acquire()						# ����con��acquire����				
		if x == 1000000:
			con.wait()					# ����con��wait����
			pass
		else:
			for i in range(1000000):
				x = x + 1
			con.notify()					# ����con��notify����
		print x
		con.release()						# ����con��release����
class Consumer(threading.Thread):					# ������������
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global x
		con.acquire()
		if x == 0:
			con.wait()	
			pass
		else:
			for i in range(1000000):
				x = x - 1
			con.notify()
		print x
		con.release()
con = threading.Condition()						# ��ʵ����
x=0
p = Producer('Producer')						# ���������߶���
c = Consumer('Consumer')						# ���������߶���
p.start()								# �����߳�
c.start()
p.join()								# �ȴ��߳̽���
c.join()
print x
