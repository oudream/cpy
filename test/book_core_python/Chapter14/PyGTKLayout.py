# -*- coding:utf-8 -*-
# file: PyGTKLayout.py
#
import pygtk											# ����pygtkģ��
pygtk.require('2.0')										# ����pygtk�����gtk�汾
import gtk											# ����gtkģ��
class MyWindow():										# ���崰����
	def __init__(self, title, width, height):						# �����ʼ������
		self.x = 10									# ����������Ϣ
		self.y = 5
		self.window = gtk.Window()							# ���ɴ��ڶ���
		self.window.set_title(title)							# ���ô��ڱ���
		self.window.set_default_size(width, height)					# ���ô��ڴ�С
		self.window.connect('destroy', lambda q: gtk.main_quit())
		self.layout = gtk.Layout()
		self.label = gtk.Label('PyGTK')							# ������ǩ
		self.layout.put(self.label,self.x,self.y)					# ��ӱ�ǩ
		self.button = gtk.Button('Move')						# ������ť
		self.button.connect('clicked',self.OnButton, 'Move')				# �󶨰�ť�¼�
		self.layout.put(self.button, 120, 150)						# ��Ӱ�ť
		self.window.add(self.layout)							# �򴰿������Layout
		self.label.show()								# ��ʾ��ǩ
		self.button.show()								# ��ʾ��ť
		self.layout.show()								# ��ʾLayout���
		self.window.show()								# ��ʾ����
	def OnButton(self, widget, data):							# ��ť�¼���Ӧ����
		self.x = self.x + 5
		self.y = self.y + 5
		if self.x >= 300:
			self.x = 10
		if self.y >= 200:
			self.y = 5
		self.layout.move(self.label, self.x, self.y)					# �ƶ���ǩ
	def main(self):										# ����main����
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# �������ڶ���
window.main()


