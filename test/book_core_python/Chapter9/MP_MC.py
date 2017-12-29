# -*- coding:utf-8 -*-
# file: MP_MC.py
#
import threading		# ����threadingģ��
import time			# ����timeģ��
import Queue			# ����Queueģ��
class Producer(threading.Thread):# ������������
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global queue	# ����queueΪȫ�ֱ���
		queue.put(self.getName())	# ����put�������߳�����ӵ�������
		print self.getName(),'put ',self.getName(),' to queue'
class Consumer(threading.Thread):# ������������
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global queue
		print self.getName(),'get ',queue.get(),'from queue'#����get������ȡ����������
queue = Queue.Queue()	# ���ɶ��ж���
plist = []		# �����߶����б�
clist = []		# �����߶����б�
for i in range(10):
	p = Producer('Producer' + str(i))
	plist.append(p)		# ��ӵ������߶����б�
for i in range(10):
	c = Consumer('Consumer' + str(i))
	clist.append(c)		# ��ӵ������߶����б�
for i in plist:
	i.start()		# �����������߳�
	i.join()
for i in clist:
	i.start()		# �����������߳�
	i.join()

