# -*- coding:utf-8 -*-
# file: HelloPyQt.py
#
import sys							# ����sysģ��
from PyQt4 import QtCore, QtGui					# ����PyQtģ��
class MyWindow(QtGui.QMainWindow):				# ͨ���̳�QtGui.QMainWindow������
	def __init__(self):					# ��ʼ������
		QtGui.QMainWindow.__init__(self)		# ���ø����ʼ������
		self.setWindowTitle('PyQt')			# ���ô��ڱ���
		self.resize(300,200)				# ���ô��ڴ�С
app = QtGui.QApplication(sys.argv)				# ����QApplication����
mywindow = MyWindow()						# ����MyWindow����
mywindow.show()							# ��ʾ����
app.exec_()							# ������Ϣѭ��
