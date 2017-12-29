# -*- coding:utf-8 -*-
# self.file: PyQtMenuAction.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QMainWindow):							# ͨ���̳�QtGui.QMainWindow������
	def __init__(self):								# ��ʼ������
		QtGui.QMainWindow.__init__(self)					# ���ø����ʼ������
		self.setWindowTitle('PyQt')						# ���ô��ڱ���
		self.resize(300,200)							# ���ô��ڴ�С
		self.label = QtGui.QLabel('Menu Action')				# ������ǩ
		self.label.setAlignment(QtCore.Qt.AlignCenter)				# ���ñ�ǩ���ֶ�����ʽ
		self.setCentralWidget(self.label)
		menubar = self.menuBar()						# ��ô��ڵĲ˵���
		self.file = menubar.addMenu('&File')					# ���File�˵�
		open = self.file.addAction('Open')					# ���Open����
		self.connect(open, QtCore.SIGNAL('triggered()'), self.OnOpen)		# �˵��ź�
		save = self.file.addAction('Save')					# ���Save����
		self.connect(save, QtCore.SIGNAL('triggered()'), self.OnSave)		# �˵��ź�
		self.file.addSeparator()						# ��ӷָ���
		close = self.file.addAction('Close')					# ���Close����
		self.connect(close, QtCore.SIGNAL('triggered()'), self.OnClose)		# �˵��ź�
	def OnOpen(self):								# ����Open����
		self.label.setText('Menu Action: Open')
	def OnSave(self):								# ����Save����
		self.label.setText('Menu Action: Save')
	def OnClose(self):								# ����Close����
		self.close()
	def contextMenuEvent(self, event):						# ���ص���ʽ�˵��¼�
        	self.file.exec_(event.globalPos())
app = QtGui.QApplication(sys.argv)							# ����QApplication����
mywindow = MyWindow()									# ����MyWindow����
mywindow.show()										# ��ʾ����
app.exec_()										# ������Ϣѭ��
