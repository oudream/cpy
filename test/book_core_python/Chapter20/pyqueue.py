# -*- coding:utf-8 -*-
# file: pyqueue.py
#
class PyQueue:									# ������
	def __init__(self, size = 20):
		self.queue = []							# ��
		self.size = size						# �Ӵ�С
		self.end = -1							# ��β
	def setSize(self, size):						# ���öӴ�С
		self.size = size
	def In(self, element):							# ���
		if self.end < self.size - 1:
			self.queue.append(element)
			self.end = self.end + 1
		else:
			raise 'PyQueueFull'					# ��������������쳣
	def Out(self):								# ����
		if self.end != -1:
			element = self.queue[0]
			self.queue = self.queue[1:]
			self.end = self.end - 1
			return element
		else:
			raise'PyQueueEmpty'					# �����Ϊ���������쳣
	def End(self):								# �����β
		return self.end
	def empty(self):							# �����
		self.queue = []
		self.end = -1
if __name__ == '__main__':
	queue = PyQueue()
	for i in range(10):
		queue.In(i)							# Ԫ�����
	print queue.End()
	for i in range(10):
		print queue.Out()						# Ԫ�س���
	for i in range(20):
		queue.In(i)							# Ԫ�����
	queue.empty()								# ��ն�
	for i in range(20):
		print queue.Out()						# �˴��������쳣
