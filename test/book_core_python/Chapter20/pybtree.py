# -*- coding:utf-8 -*-
# file: pybtree.py
#
class BTree:									# �������ڵ�
	def __init__(self, value):						# ��ʼ������
		self.left = None						# �����
		self.data = value						# �ڵ�ֵ
		self.right = None						# �Ҷ���
	def insertLeft(self, value):						# ������������ڵ�
		self.left = BTree(value)
		return self.left
	def insertRight(self, value):						# ������������ڵ�
		self.right = BTree(value)
		return self.right
	def show(self):								# ����ڵ�����
		print self.data
if __name__ == '__main__':
	Root = BTree('Root')							# ���ڵ�
	A = Root.insertLeft('A')						# ����ڵ��в���A�ڵ�
	C = A.insertLeft('C')							# ��A�ڵ��в���C�ڵ�
	D = A.insertRight('D')							# ��A�ڵ��в���D�ڵ�
	F = D.insertLeft('F')							# ��D�ڵ��в���F�ڵ�
	G = D.insertRight('G')							# ��D�ڵ��в���G�ڵ�
	B = Root.insertRight('B')						# ����ڵ��в���B�ڵ�
	E = B.insertRight('E')							# ��B�ڵ��в���E�ڵ�
	Root.show()								# ����ڵ�����
	Root.left.show()
	Root.right.show()
	A = Root.left
	A.left.show()
	Root.left.right.show()

