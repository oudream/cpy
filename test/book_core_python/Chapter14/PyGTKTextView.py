# -*- coding:utf-8 -*-
# file: PyGTKTextView.py
#
import pygtk											# ����pygtkģ��
pygtk.require('2.0')										# ����pygtk�����gtk�汾
import gtk											# ����gtkģ��
class MyWindow():										# ���崰����
	def __init__(self, title, width, height):						# �����ʼ������
		self.window = gtk.Window()							# ���ɴ��ڶ���
		self.window.set_title(title)							# ���ô��ڱ���
		self.window.set_default_size(width, height)					# ���ô��ڴ�С
		self.window.connect('destroy', lambda q: gtk.main_quit())			# �رմ���ʱ�˳�����
		vbox = gtk.VBox(False, 5)							# ��������Box����
		swindow = gtk.ScrolledWindow()
		text = gtk.TextView()								# ���������ı���
		textbuffer = text.get_buffer()							# �ı��򻺳���
		swindow.add(text)
	        swindow.show()
		vbox.pack_start(swindow)							# ��Box����������ı���
		text.show()									# ��ʾ�ı���
		self.window.add(vbox)								# �򴰿����Box����
		vbox.show()
		self.window.show()								# ��ʾ����
	def main(self):										# ����main����
		gtk.main()									# ����gtk.main����
window = MyWindow('PyGTK', 300, 200)								# �������ڶ���
window.main()
