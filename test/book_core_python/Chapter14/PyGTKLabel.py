# -*- coding:utf-8 -*-
# file: PyGTKLabel.py
#
import pygtk											# ����pygtkģ��
pygtk.require('2.0')										# ����pygtk�����gtk�汾
import gtk											# ����gtkģ��
class MyWindow():										# ���崰����
	def __init__(self, title, width, height):						# �����ʼ������
		self.window = gtk.Window()							# ���ɴ��ڶ���
		self.window.set_title(title)							# ���ô��ڱ���
		self.window.set_default_size(width, height)					# ���ô��ڴ�С
		label = gtk.Label('PyGTK')							# ������ǩ
		label.set_angle(90)								# ���ñ�ǩ�Ƕ�
		self.window.add(label)								# �򴰿�����ӱ�ǩ
		label.show()									# ��ʾ��ǩ
		self.window.show()								# ��ʾ����
	def main(self):										# ����main����
		gtk.main()									# ����gtk.main����
window = MyWindow('PyGTK', 300, 200)								# �������ڶ���
window.main()
