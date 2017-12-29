# -*- coding:utf-8 -*-
# file: PyQtLineEdit.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):							# ͨ���̳�QtGui.QWidget������
	def __init__(self):							# ��ʼ������
		QtGui.QWidget.__init__(self)					# ���ø����ʼ������
		self.setWindowTitle('PyQt')					# ���ô��ڱ���
		self.resize(300,200)						# ���ô��ڴ�С
		gridlayout = QtGui.QGridLayout()				# �����������
		label1 = QtGui.QLabel('Normal Lineedit')			# ������ǩ
		label1.setAlignment(QtCore.Qt.AlignCenter)
		gridlayout.addWidget(label1, 0, 0 )
		edit1 = QtGui.QLineEdit()					# ���������ı���
		gridlayout.addWidget(edit1, 1, 0)
		label2 = QtGui.QLabel('Password')				# ������ǩ
		label2.setAlignment(QtCore.Qt.AlignCenter)
		gridlayout.addWidget(label2, 2, 0)
		edit2 = QtGui.QLineEdit()					# ���������ı���
		edit2.setEchoMode(QtGui.QLineEdit.Password)			# ��������Ϊ�����
		gridlayout.addWidget(edit2, 3, 0)
		self.setLayout(gridlayout)	
app = QtGui.QApplication(sys.argv)						# ����QApplication����
mywindow = MyWindow()								# ����MyWindow����
mywindow.show()									# ��ʾ����
app.exec_()									# ������Ϣѭ��
