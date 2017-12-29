# -*- coding:utf-8 -*-
# file: PyGTKEntry.py
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
		label1 = gtk.Label('Nomal')							# ������ǩ
		vbox.pack_start(label1)								# ��Box��������ӱ�ǩ
		entry1 = gtk.Entry()								# �����ı���
		vbox.pack_start(entry1)								# ��Box����������ı���
		entry1.show()									# ��ʾ�ı���
		label2 = gtk.Label('Password')							# ������ǩ
		vbox.pack_start(label2)	
		entry2 = gtk.Entry()								# �����ı���
		entry2.set_visibility(False)							# ���ı�������Ϊ�����
		vbox.pack_start(entry2)
		entry2.show()
		self.window.add(vbox)								# �򴰿����Box����
		label1.show()									# ��ʾ��ǩ
		label2.show()
		vbox.show()
		self.window.show()								# ��ʾ����
	def main(self):										# ����main����
		gtk.main()									# ����gtk.main����
window = MyWindow('PyGTK', 200, 120)								# �������ڶ���
window.main()
