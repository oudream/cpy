# -*- coding:utf-8 -*-
# file: PyGTKButton.py
#
import pygtk											# ����pygtkģ��
pygtk.require('2.0')										# ����pygtk�����gtk�汾
import gtk											# ����gtkģ��
class MyWindow():										# ���崰����
	def __init__(self, title, width, height):						# �����ʼ������
		self.window = gtk.Window()							# ���ɴ��ڶ���
		self.window.set_title(title)							# ���ô��ڱ���
		self.window.set_default_size(width, height)					# ���ô��ڴ�С
       		hbox = gtk.HBox(False, 20)							# ����ˮƽBox����
		button1 = gtk.Button('Button1')							# ������ť
		button2 = gtk.Button('Button2')
		hbox.pack_start(button1)							# ��Box��������Ӱ�ť
		hbox.pack_start(button2)
		self.window.add(hbox)								# �򴰿����Box����
		hbox.show()									# ��ʾBox����
		button1.show()									# ��ʾ��ť
		button2.show()
		self.window.show()								# ��ʾ����
	def main(self):										# ����main����
		gtk.main()									# ����gtk.main����
window = MyWindow('PyGTK', 150, 30)								# �������ڶ���
window.main()
