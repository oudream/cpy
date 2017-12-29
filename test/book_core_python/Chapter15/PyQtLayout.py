# -*- coding:utf-8 -*-
# file: PyQtLayout.py
#
import sys							# ����sysģ��
from PyQt4 import QtCore, QtGui					# ����PyQtģ��
class MyWindow(QtGui.QWidget):					# ͨ���̳�QtGui.QWidget������
	def __init__(self):					# ��ʼ������
		QtGui.QWidget.__init__(self)			# ���ø����ʼ������
		self.setWindowTitle('PyQt')			# ���ô��ڱ���
		self.resize(300,200)				# ���ô��ڴ�С
		gridlayout = QtGui.QGridLayout()		# �����������
		hboxlayout1 = QtGui.QHBoxLayout()
		hboxlayout2 = QtGui.QHBoxLayout()
		vboxlayout1 = QtGui.QVBoxLayout()
		vboxlayout2 = QtGui.QVBoxLayout()
		label1 = QtGui.QLabel('Label1',self)		# ������ǩ
		label1.setAlignment(QtCore.Qt.AlignCenter)
		label2 = QtGui.QLabel('Label2')
		label3 = QtGui.QLabel('Label3')
		label4 = QtGui.QLabel('Label4')
		label5 = QtGui.QLabel('Label5')
		hboxlayout1.addWidget(label1)			# �򲼾��������ӱ�ǩ
		vboxlayout1.addWidget(label2)
		vboxlayout1.addWidget(label3)
		vboxlayout2.addWidget(label4)
		vboxlayout2.addWidget(label5)
		hboxlayout2.addLayout(vboxlayout1)		# ��hboxlayout2���vboxlayout1
		hboxlayout2.addLayout(vboxlayout2)		# ��hboxlayout2���vboxlayout2
		gridlayout.addLayout(hboxlayout1, 0 ,0)		# ���һ�е�һ�����hboxlayout1
		gridlayout.addLayout(hboxlayout2, 1, 0)		# ��ڶ��е�һ�����hboxlayout2
		gridlayout.setRowMinimumHeight (1, 180)		# ���õڶ��е���С�߶�Ϊ108
		self.setLayout(gridlayout)
app = QtGui.QApplication(sys.argv)				# ����QApplication����
mywindow = MyWindow()						# ����MyWindow����
mywindow.show()							# ��ʾ����
app.exec_()							# ������Ϣѭ��
