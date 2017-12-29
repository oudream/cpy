# -*- coding:utf-8 -*-
# file: PyGTKRCbutton.py
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
		self.label1 = gtk.Label('PyGTK')						# ������ǩ
		self.fixed.put(self.label1, 80, 20)						# ��ӱ�ǩ
		self.label2 = gtk.Label('PyGTK')
		self.fixed.put(self.label2, 160, 20)						# ��ӵ�ѡ��
		self.radio1 = gtk.RadioButton(None, 'Radio1')
		self.fixed.put(self.radio1, 50, 60)
		self.radio2 = gtk.RadioButton(self.radio1, 'Radio2')
		self.fixed.put(self.radio2, 50, 90)
		self.radio3 = gtk.RadioButton(self.radio1, 'Radio3')
		self.fixed.put(self.radio3, 50, 120)
		self.check = gtk.CheckButton('CheckButton')
		self.fixed.put(self.check, 150, 60)
		self.button = gtk.Button('Test')						# ������ť
		self.button.connect('clicked',self.OnButton, 'Test')				# �󶨰�ť�¼�
		self.fixed.put(self.button, 120, 150)						# ��Ӱ�ť
		self.window.add(self.fixed)							# �򴰿������Fixed
		self.label1.show()								# ��ʾ���
		self.label2.show()
		self.radio1.show()
		self.radio2.show()
 		self.radio3.show()
		self.check.show()
		self.button.show()
		self.fixed.show()
		self.window.show()
	def OnButton(self, widget, data):
		if self.check.get_active():							# �жϸ�ѡ���Ƿ�ѡ��
			self.label2.set_text('checked')
		else:
			self.label2.set_text('uncheck')
		if self.radio1.get_active():							# �жϸ�ѡ��ѡ��״̬
			self.label1.set_text('Radio1')
		elif self.radio2.get_active():
			self.label1.set_text('Radio2')
		else:
			self.label1.set_text('Radio3')
	def main(self):										# ����main����
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# �������ڶ���
window.main()


