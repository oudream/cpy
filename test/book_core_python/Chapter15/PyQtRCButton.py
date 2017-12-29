# -*- coding:utf-8 -*-
# file: PyQtRCButton.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):
	def __init__(self):							# ��ʼ������
		QtGui.QWidget.__init__(self)					# ���ø����ʼ������
		self.setWindowTitle('PyQt')					# ���ô��ڱ���
		self.resize(300,200)						# ���ô��ڴ�С
		gridlayout = QtGui.QGridLayout()				# �����������
		self.label1 = QtGui.QLabel('Label1')				# ������ǩ
		self.label2 = QtGui.QLabel('Label2')
		gridlayout.addWidget(self.label1, 1, 2)
		gridlayout.addWidget(self.label2, 2, 2)
        	self.radio1 = QtGui.QRadioButton('Radio1')			# ������ѡ��
        	self.radio2 = QtGui.QRadioButton('Radio2')
		self.radio3 = QtGui.QRadioButton('Radio3')
		self.radio1.setChecked(True)					# ��Radio1ѡ��
		gridlayout.addWidget(self.radio1, 1, 1 )			# ��ӵ�ѡ��
		gridlayout.addWidget(self.radio2, 2, 1 )
		gridlayout.addWidget(self.radio3, 3, 1 )
		self.check = QtGui.QCheckBox('check')				# ������ѡ��
		self.check.setChecked(True)					# ����ѡ��ѡ��
		gridlayout.addWidget(self.check, 3, 2)
		self.button = QtGui.QPushButton('Test')				# ������ť
		gridlayout.addWidget(self.button, 4, 1, 1, 2)
		self.setLayout(gridlayout)					# �򴰿�����Ӳ������
		self.connect(self.button, 					# ��ť�¼�
				QtCore.SIGNAL('clicked()'),
				self.OnButton)
	def OnButton(self):							# ��ť��ۺ���
		if self.radio1.isChecked():					# �жϵ�ѡ���Ƿ�ѡ��
			self.label1.setText('Radio1')
		elif self.radio2.isChecked():
			self.label1.setText('Radio2')
		else :
			self.label1.setText('Radio3')
		if self.check.isChecked():					# �жϸ�ѡ���Ƿ�ѡ��
			self.label2.setText('checked')
		else:
			self.label2.setText('uncheck')
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()		
mywindow.show()		
app.exec_()	
