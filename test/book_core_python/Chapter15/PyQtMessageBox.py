# -*- coding:utf-8 -*-
# file: PyQtMessageBox.py
#
import sys
from PyQt4 import QtCore, QtGui	
class MyWindow(QtGui.QWidget):
	def __init__(self):							# ��ʼ������
		QtGui.QWidget.__init__(self)					# ���ø����ʼ������
		self.setWindowTitle('PyQt')					# ���ô��ڱ���
		self.resize(300,200)						# ���ô��ڴ�С
		gridlayout = QtGui.QGridLayout()				# �����������
		self.label = QtGui.QLabel('MessBox example')
		gridlayout.addWidget(self.label, 1, 3, 1, 3)
		self.button1 = QtGui.QPushButton('About')			# ����Button1
		gridlayout.addWidget(self.button1, 2, 1)
		self.button2 = QtGui.QPushButton('AboutQt')			# ����Button2
		gridlayout.addWidget(self.button2, 2, 2)
		self.button3 = QtGui.QPushButton('Critical')			# ����Button2
		gridlayout.addWidget(self.button3, 2, 3)
		self.button4 = QtGui.QPushButton('Info')			# ����Button2
		gridlayout.addWidget(self.button4, 2, 4)
		self.button5 = QtGui.QPushButton('Qusetion')			# ����Button2
		gridlayout.addWidget(self.button5, 2, 5)
		self.button6 = QtGui.QPushButton('Warning')			# ����Button2
		gridlayout.addWidget(self.button6, 2, 6)
		spacer = QtGui.QSpacerItem(200, 80)
		gridlayout.addItem(spacer, 3, 1, 1, 5)
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
		self.connect(self.button4, 					# Button4�¼�
				QtCore.SIGNAL('clicked()'), 
				self.OnButton4)
		self.connect(self.button5, 					# Button5�¼�
				QtCore.SIGNAL('clicked()'), 
				self.OnButton5)
		self.connect(self.button6, 					# Button6�¼�
				QtCore.SIGNAL('clicked()'),
				self.OnButton6)	
	def OnButton1(self):							# Button1��ۺ���
		self.button1.setText('clicked')
		QtGui.QMessageBox.about(self, 'PyQt', 'About')			# ����About��Ϣ��
	def OnButton2(self):							# Button2��ۺ���
		self.button2.setText('clicked')
		QtGui.QMessageBox.aboutQt(self, 'PyQt')				# ����AboutQt��Ϣ��
	def OnButton3(self):							# Button3��ۺ���
		self.button3.setText('clicked')
        	r = QtGui.QMessageBox.critical(self, 'PyQt',			# ����Ctitical��Ϣ��
				'Critical', 
				QtGui.QMessageBox.Abort,
				QtGui.QMessageBox.Retry,
				QtGui.QMessageBox.Ignore)
        	if r == QtGui.QMessageBox.Abort:
            		self.label.setText('Abort')
        	elif r == QtGui.QMessageBox.Retry:
           		self.label.setText('Retry')
        	else:
            		self.label.setText('Ignore')
	def OnButton4(self):							# Button4��ۺ���
		self.button4.setText('clicked')
		QtGui.QMessageBox.information(self, 'PyQt', 'Information')	# ����Information��Ϣ��
	def OnButton5(self):							# Button5��ۺ���
		self.button5.setText('clicked')
        	r = QtGui.QMessageBox.question(self, 'PyQt',			# ����Question��Ϣ��
				'Question', 
				QtGui.QMessageBox.Yes,
				QtGui.QMessageBox.No,
				QtGui.QMessageBox.Cancel)
	def OnButton6(self):							# Button6��ۺ���
		self.button6.setText('clicked')
       		r = QtGui.QMessageBox.warning(self, 'PyQt',			# ����Warning��Ϣ��
				'Warning', 
				QtGui.QMessageBox.Yes,
				QtGui.QMessageBox.No)
app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()

