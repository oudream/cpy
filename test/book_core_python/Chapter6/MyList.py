# -*- coding:utf-8 -*-
# file: MyList.py
#
class MyList:									# ����MyList��
	#__mylist = []									# ����__mylist����
	def __init__(self, *args):							# ����__init__����
		self.__mylist = []					# �˴��൱��__mylist��ʼ����������ʵ���������ݻ��
		for arg in args:
			self.__mylist.append(arg)
	def __add__(self,n):								# ���ء�+�������
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] + n
	def __sub__(self,n):								# ���ء�-�������
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] - n
	def __mul__(self,n):								# ���ء�*�������
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] * n
	def __div__(self,n):								# ���ء�/�������
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] / n
	def __mod__(self,n):								# ���ء�%�������
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] % n
	def __pow__(self,n):								# ���ء�**�������
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] ** n
	def __len__(self):								# ����len����
		return len(self.__mylist)
	def show(self):									# ����show����
		print self.__mylist
		


