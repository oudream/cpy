# -*- coding:utf-8 -*-
# file: event.py
#
import threading			# ����threadingģ��
class mythread(threading.Thread):
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global event		# ʹ��ȫ��Event����
		if event.isSet():	# �ж�Event�����ڲ��źű�־
			event.clear()	# �������ñ�־�����
			event.wait()	# ����wait����
			print self.getName()
		else:
			print self.getName()
			event.set()	# ����Event�����ڲ��źű�־
event = threading.Event()		# ����Event����
event.set()				# ����Event�����ڲ��źű�־
tl = []
for i in range(10):
	t = mythread(str(i))
	tl.append(t)			# �����߳��б�
	
for i in tl:
	i.start()			# �����߳�
