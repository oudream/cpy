# -*- coding:utf-8 -*-
# file: PyGTKGlade.py
#
import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade
class MyWindow():							# ���崰����
	def __init__(self):						# �����ʼ������
	        res = gtk.glade.XML('res.glade') 			# ������Դ�ļ�������gtk.glade.XMLʵ������
		window = res.get_widget('window')			# ����window
		signal = { 'OnQuit' : self.OnQuit }			# �����ź��ֵ�
		res.signal_autoconnect(signal)				# ���ź��¼�
		window.connect('destroy', lambda q:gtk.main_quit())	# ���ڹر����˳�����
		window.show()
	def OnQuit(self, widget):					# Quit�˵�������¼�
		gtk.main_quit()
	def main(self):							# ����main����
		gtk.main()						# ����gtk.main����
window = MyWindow()							# �������ڶ���
window.main()			
