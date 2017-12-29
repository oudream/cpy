# -*- coding:utf-8 -*-
# file: PyQtMenu.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QMainWindow):						# ͨ���̳�QtGui.QMainWindow������
	def __init__(self):							# ��ʼ������
		QtGui.QMainWindow.__init__(self)				# ���ø����ʼ������
		self.setWindowTitle('PyQt')					# ���ô��ڱ���
		self.resize(300,200)						# ���ô��ڴ�С
		menubar = self.menuBar()					# ��ô��ڵĲ˵���
		file = menubar.addMenu('&File')					# ���File�˵�
		file.addAction('Open')						# ���Open����
		file.addAction('Save')						# ���Save����
		file.addSeparator()						# ��ӷָ���
		file.addAction('Close')						# ���Close����
		edit = menubar.addMenu('&Edit')					# ���Edit�˵�
		edit.addAction('Copy')						# ���Copy����
		edit.addAction('Paste')						# ���Paste����
		edit.addAction('Cut')						# ���Cut����
		edit.addAction('SelectAll')					# ���SelectAll����
		help = menubar.addMenu('&Help')					# ���Help�˵�
		help.addAction('About')						# ���About����
app = QtGui.QApplication(sys.argv)						# ����QApplication����
mywindow = MyWindow()								# ����MyWindow����
mywindow.show()									# ��ʾ����
app.exec_()									# ������Ϣѭ��
