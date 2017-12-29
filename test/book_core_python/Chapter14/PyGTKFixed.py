# -*- coding:utf-8 -*-
# file: PyGTKFixed.py
#
import pygtk											# ����pygtkģ��
pygtk.require('2.0')										# ����pygtk�����gtk�汾
import gtk											# ����gtkģ��
class MyWindow():										# ���崰����
	def __init__(self, title, width, height):						# �����ʼ������
		self.window = gtk.Window()							# ���ɴ��ڶ���
		self.window.set_title(title)							# ���ô��ڱ���
		self.window.set_default_size(width, height)					# ���ô��ڴ�С
		self.window.connect('destroy', lambda q: gtk.main_quit())
		self.fixed = gtk.Fixed()
		self.label = gtk.Label('PyGTK')							# ������ǩ
		self.fixed.put(self.label,10,5)							# ��ӱ�ǩ
		self.button = gtk.Button('Move')						# ������ť
		self.button.connect('clicked',self.OnButton, 'Move')				# �󶨰�ť�¼�
		self.fixed.put(self.button, 120, 150)						# ��Ӱ�ť
		self.window.add(self.fixed)							# �򴰿������Fixed
		self.label.show()								# ��ʾ��ǩ
		self.button.show()								# ��ʾ��ť
		self.fixed.show()								# ��ʾFixed���
		self.window.show()								# ��ʾ����
	def OnButton(self, widget, data):
		self.fixed.move(self.label, 100,50)
	def main(self):										# ����main����
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# �������ڶ���
window.main()

