# -*- coding:utf-8 -*-
# file: syn.py
#
import threading							# ����threadingģ��
import time								# ����timeģ��
class mythread(threading.Thread):					# ͨ���̳д�����
	def __init__(self,threadname):					# ��ʼ������
		threading.Thread.__init__(self,name = threadname)	# ���ø���ĳ�ʼ������
	def run(self):							# ����run����
		global x						# ʹ��global����xΪȫ�ֱ���
		lock.acquire()						# ����lock��acquire����
		for i in range(3):
			x = x + 1
		time.sleep(2)						# ����sleep���������߳�����5��
		print x
		lock.release()						# ����lock��release����
lock = threading.RLock()						# ��ʵ����	
tl = []									# �����б�
for i in range(10):
	t = mythread(str(i))						# ��ʵ����
	tl.append(t)							# ���������ӵ��б���
	
x=0									# ��x��ֵΪ0
for i in tl:
	i.start()							# ���������߳�


