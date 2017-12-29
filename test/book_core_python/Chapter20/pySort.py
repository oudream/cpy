# -*- coding:utf-8 -*-
# file: pySort.py
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
def inorder(node):								# �������
	if node.data:
		if node.left:
			inorder(node.left)
		node.show()
		if node.right:
			inorder(node.right)
def rinorder(node):								# �������,�ȱ���������
	if node.data:
		if node.right:
			rinorder(node.right)
		node.show()
		if node.left:
			rinorder(node.left)
def insert(node, value):
	if value > node.data:
		if node.right:
			insert(node.right, value)
		else:
			node.insertRight(value)
	else:
		if node.left:
			insert(node.left, value)
		else:
			node.insertLeft(value)
if __name__ == '__main__':
	l = [3, 5 , 7, 20, 43, 2, 15, 30]
	Root = BTree(l[0])							# ���ڵ�
	node = Root
	for i in range(1, len(l)):
		insert(Root, l[i])
	print '*****************************'
	print '        ��С����'
	print '*****************************'
	inorder(Root)
	print '*****************************'
	print '        �Ӵ�С'
	print '*****************************'
	rinorder(Root)
