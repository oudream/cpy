# -*- coding:utf-8 -*-
# file: TreeTraversal.py
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
def preorder(node):								# �������
	if node.data:
		node.show()
		if node.left:
			preorder(node.left)
		if node.right:
			preorder(node.right)
def inorder(node):								# �������
	if node.data:
		if node.left:
			inorder(node.left)
		node.show()
		if node.right:
			inorder(node.right)
def postorder(node):								# �������
	if node.data:
		if node.left:
			postorder(node.left)
		if node.right:
			postorder(node.right)
		node.show()
if __name__ == '__main__':
	Root = BTree('Root')							# ������
	A = Root.insertLeft('A')
	C = A.insertLeft('C')
	D = A.insertRight('D')
	F = D.insertLeft('F')
	G = D.insertRight('G')
	B = Root.insertRight('B')
	E = B.insertRight('E')
	print '*************************'
	print 'Binary Tree Pre-Traversal'
	print '*************************'
	preorder(Root)								# ���������������
	print '*************************'
	print 'Binary Tree In-Traversal'
	print '*************************'
	inorder(Root)								# ���������������
	print '*************************'
	print 'Binary Tree Post-Traversal'
	print '*************************'
	postorder(Root)								# �������к������
