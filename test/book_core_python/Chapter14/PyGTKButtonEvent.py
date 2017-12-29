# -*- coding:utf-8 -*-
# file: PyGTKButtonEvent.py
#
import pygtk											# ����pygtkģ��
pygtk.require('2.0')										# ����pygtk�����gtk�汾
import gtk											# ����gtkģ��
class MyWindow():										# ���崰����
	def __init__(self, title, width, height):						# �����ʼ������
		self.window = gtk.Window()							# ���ɴ��ڶ���
		self.window.set_title(title)							# ���ô��ڱ���
		self.window.set_default_size(width, height)					# ���ô��ڴ�С
		self.window.connect('destroy', lambda w: gtk.main_quit())			# �رմ���ʱ�˳�����
       		hbox = gtk.HBox(False, 20)							# ����ˮƽBox����
		self.button1 = gtk.Button('Button1')						# ������ť
		self.button2 = gtk.Button('Button2')
		self.button1.connect('clicked', self.OnButton1, 'Button1')			# �󶨰�ť�¼�
		self.button2.connect('clicked', self.OnButton2, 'Button2')
		hbox.pack_start(self.button1)							# ��Box��������Ӱ�ť
		hbox.pack_start(self.button2)
		self.window.add(hbox)								# �򴰿����Box����
		hbox.show()									# ��ʾBox����
		self.button1.show()								# ��ʾ��ť
		self.button2.show()
		self.window.show()								# ��ʾ����
	def main(self):										# ����main����
		gtk.main()									# ����gtk.main����
	def OnButton1(self,widget, data):							# ����ť�¼�
		self.button2.set_label('Quit')							# ��������Button2�ı�
	def OnButton2(self, widgte, data):							# ����ť�¼�
		gtk.main_quit()									# �˳�����
window = MyWindow('PyGTK', 150, 30)								# �������ڶ���
window.main()
