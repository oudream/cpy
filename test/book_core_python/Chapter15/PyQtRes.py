# -*- coding:utf-8 -*-
# file: PyQtRes.py
#
import sys
from PyQt4 import QtCore, QtGui, uic	
class MyDialog(QtGui.QDialog):							# �̳�QtGui.QDialog
    	def __init__(self):
		QtGui.QWidget.__init__(self)
        	uic.loadUi("res.ui", self)	

class MyWindow(QtGui.QWidget):
	def __init__(self):							# ��ʼ������
		QtGui.QWidget.__init__(self)					# ���ø����ʼ������
		self.setWindowTitle('PyQt')					# ���ô��ڱ���
		self.resize(300,200)						# ���ô��ڴ�С
		gridlayout = QtGui.QGridLayout()				# �����������
		self.button = QtGui.QPushButton('CreateDialog')			# ����Button1
		gridlayout.addWidget(self.button, 1, 1)
		self.setLayout(gridlayout)					# �򴰿�����Ӳ������
		self.connect(self.button, 					# Button�¼�
				QtCore.SIGNAL('clicked()'),
				self.OnButton)
	def OnButton(self):							# ����ť�¼�		
		dialog = MyDialog()						# �����Ի������
		r = dialog.exec_()						# ���жԻ���
		if r:
			self.button.setText(dialog.lineEdit.text())
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
