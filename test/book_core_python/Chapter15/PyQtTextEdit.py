# -*- coding:utf-8 -*-
# file: PyQtTextEdit.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):							# ͨ���̳�QtGui.QWidget������
	def __init__(self):							# ��ʼ������
		QtGui.QWidget.__init__(self)					# ���ø����ʼ������
		self.setWindowTitle('PyQt')					# ���ô��ڱ���
		self.resize(300,200)						# ���ô��ڴ�С
		gridlayout = QtGui.QGridLayout()				# �����������
		label = QtGui.QLabel('TextEdit')				# ������ǩ
		label.setAlignment(QtCore.Qt.AlignCenter)
		gridlayout.addWidget(label, 0, 0 )
		edit = QtGui.QTextEdit()					# ���������ı���
		edit.setText('Python\nPyQt')					# �����ı����е�����
		gridlayout.addWidget(edit, 1, 0)
		self.setLayout(gridlayout)	
app = QtGui.QApplication(sys.argv)						# ����QApplication����
mywindow = MyWindow()								# ����MyWindow����
mywindow.show()									# ��ʾ����
app.exec_()									# ������Ϣѭ��

