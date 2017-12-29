# -*- coding:utf-8 -*-
# file: PyQtSpacer.py
#
import sys							# ����sysģ��
from PyQt4 import QtCore, QtGui					# ����PyQtģ��
class MyWindow(QtGui.QWidget):					# ͨ���̳�QtGui.QWidget������
	def __init__(self):					# ��ʼ������
		QtGui.QWidget.__init__(self)			# ���ø����ʼ������
		self.setWindowTitle('PyQt')			# ���ô��ڱ���
		self.resize(300,200)				# ���ô��ڴ�С
		gridlayout = QtGui.QGridLayout()		# �����������
		spacer1 = QtGui.QSpacerItem(300,40)		# �����հ���
		spacer2 = QtGui.QSpacerItem(300,40)
		label = QtGui.QLabel('Label',self)		# ������ǩ
		label.setAlignment(QtCore.Qt.AlignCenter)
		gridlayout.addItem(spacer1, 0 ,0)		# ��ӿհ���
		gridlayout.addWidget(label, 1, 0)		# ��ӱ�ǩ
		gridlayout.addItem(spacer2, 2, 0)		# ��ӿհ���
		self.setLayout(gridlayout)
app = QtGui.QApplication(sys.argv)				# ����QApplication����
mywindow = MyWindow()						# ����MyWindow����
mywindow.show()							# ��ʾ����
app.exec_()							# ������Ϣѭ��
