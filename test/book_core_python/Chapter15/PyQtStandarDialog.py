# -*- coding:utf-8 -*-
# file: PyQtStandarDialog.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):
	def __init__(self):							# ��ʼ������
		QtGui.QWidget.__init__(self)					# ���ø����ʼ������
		self.setWindowTitle('PyQt')					# ���ô��ڱ���
		self.resize(300,200)						# ���ô��ڴ�С
		gridlayout = QtGui.QGridLayout()				# �����������
		self.label = QtGui.QLabel('StandarDialog example')
		gridlayout.addWidget(self.label, 1, 2)
		self.button1 = QtGui.QPushButton('File')			# ����Button1
		gridlayout.addWidget(self.button1, 2, 1)
		self.button2 = QtGui.QPushButton('Font')			# ����Button2
		gridlayout.addWidget(self.button2, 2, 2)
		self.button3 = QtGui.QPushButton('Color')			# ����Button2
		gridlayout.addWidget(self.button3, 2, 3)
		spacer = QtGui.QSpacerItem(200, 80)
		gridlayout.addItem(spacer, 3, 1, 1, 3)
		self.setLayout(gridlayout)					# �򴰿�����Ӳ������
		self.connect(self.button1, 					# Button1�¼�
				QtCore.SIGNAL('clicked()'),
				self.OnButton1)
		self.connect(self.button2, 					# Button2�¼�
				QtCore.SIGNAL('clicked()'),
				self.OnButton2)
		self.connect(self.button3, 					# Button3�¼�
				QtCore.SIGNAL('clicked()'),
				self.OnButton3)
	def OnButton1(self):			
		self.button1.setText('clicked')
		filename = QtGui.QFileDialog.getOpenFileName(self, 'Open')	# �����ļ��򿪶Ի���
        	if not filename.isEmpty():
            		self.label.setText(filename)
	def OnButton2(self):							# Button2��ۺ���
		self.button2.setText('clicked')
		font, ok = QtGui.QFontDialog.getFont()				# ��������ѡ�жԻ���
		if ok:
			self.label.setText(font.key())
	def OnButton3(self):							# Button3��ۺ���
		self.button3.setText('clicked')
		color = QtGui.QColorDialog.getColor()				# ������ɫѡ��Ի���
		if color.isValid(): 
			self.label.setText(color.name())
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
