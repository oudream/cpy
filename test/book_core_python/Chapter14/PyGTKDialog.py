# -*- coding:utf-8 -*-
# file: PyGTKDialog.py
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
		self.label = gtk.Label('Dialog Example')					# ������ǩ
		self.fixed.put(self.label, 80, 40)						# ��ӱ�ǩ
		self.button = gtk.Button('CreateDialog')					# ������ť
		self.button.connect('clicked',self.OnButton, 'CreateDialog')			# �󶨰�ť�¼�
		self.fixed.put(self.button, 80, 130)						# ��Ӱ�ť
		self.window.add(self.fixed)							# �򴰿������Fixed
		self.label.show()								# ��ʾ���
		self.button.show()
		self.fixed.show()
		self.window.show()
	def OnButton(self, widget, data):							# ��ť�¼�������
		dialog = gtk.Dialog('PyGTK', 							# �����Ի���
				None,								# �Ի��򸸴���
				gtk.DIALOG_MODAL,						# �Ի����־
                     		(gtk.STOCK_CANCEL, 						# ��Ի��������Cancel��ť
				gtk.RESPONSE_CANCEL,						# Cancel��ť�ķ���ֵ
                      		gtk.STOCK_OK, 							# ��Ի��������Ok��ť
				gtk.RESPONSE_OK))						# Ok��ť�ķ���ֵ
		fixed = gtk.Fixed()								# ����Fixed���
		dialog.vbox.pack_start(fixed)							# ��Ի����е�vbox���Fixed���
		label = gtk.Label('Input')							# ������ǩ
		fixed.put(label,10,5)								# ��Fixed�������ӱ�ǩ
		entry = gtk.Entry()								# �����ı���
		fixed.put(entry,50,5)								# ��Fixed���������ı���
		fixed.show()									# ��ʾ�����
		label.show()
		entry.show()
		r = dialog.run()								# ��ʾ�Ի��򲢻�ȡ�䷵��ֵ
		if r == gtk.RESPONSE_OK:							# ������Ok��ť������ı����е�����
			print entry.get_text()
		dialog.destroy()
	def main(self):										# ����main����
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# �������ڶ���
window.main()
