# -*- coding:utf-8 -*-
# file: PyQtButtonEvent.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):
	def __init__(self):							# ��ʼ������
		QtGui.QWidget.__init__(self)					# ���ø����ʼ������
		self.setWindowTitle('PyQt')					# ���ô��ڱ���
		self.resize(300,200)						# ���ô��ڴ�С
		gridlayout = QtGui.QGridLayout()				# �����������
		self.button1 = QtGui.QPushButton('Button1')			# ����Button1
		gridlayout.addWidget(self.button1, 1, 1, 1 ,3)
		self.button2 = QtGui.QPushButton('Button2')			# ����Button2
		gridlayout.addWidget(self.button2, 2, 2)
		self.setLayout(gridlayout)					# �򴰿�����Ӳ������
		self.connect(self.button1, 					# Button1�¼�
				QtCore.SIGNAL('clicked()'), 			# clicked()�ź�
				self.OnButton1)					# ��ۺ���
		self.connect(self.button2, 					# Button2�¼�
				QtCore.SIGNAL('clicked()'), 			# clicked()�ź�
				self.OnButton2)					# ��ۺ���
	def OnButton1(self):							# Button1��ۺ���
		self.button1.setText('clicked')
	def OnButton2(self):							# Button2��ۺ���
		self.button2.setText('clicked')
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()		
mywindow.show()		
app.exec_()	
