# -*- coding:utf-8 -*-
# file: PyQtButton.py
#
import sys									# ����sysģ��
from PyQt4 import QtCore, QtGui							# ����PyQtģ��
class MyWindow(QtGui.QWidget):							# ͨ���̳�QtGui.QWidget������
	def __init__(self):							# ��ʼ������
		QtGui.QWidget.__init__(self)					# ���ø����ʼ������
		self.setWindowTitle('PyQt')					# ���ô��ڱ���
		self.resize(300,200)						# ���ô��ڴ�С
		gridlayout = QtGui.QGridLayout()				# �����������
		button1 = QtGui.QPushButton('Button1')				# ����Button1
		gridlayout.addWidget(button1, 1, 1, 1 ,3)			# ���Button1
		button2 = QtGui.QPushButton('Button2')				# ����Button2
		button2.setFlat(True)
		gridlayout.addWidget(button2, 2, 2)				# ���Button2
		self.setLayout(gridlayout)					# �򴰿�����Ӳ������
app = QtGui.QApplication(sys.argv)						# ����QApplication����
mywindow = MyWindow()								# ����MyWindow����
mywindow.show()									# ��ʾ����
app.exec_()									# ������Ϣѭ��
