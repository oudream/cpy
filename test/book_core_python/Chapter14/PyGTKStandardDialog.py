# -*- coding:utf-8 -*-
# file: PyGTKStandardDialog.py
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
		self.label1 = gtk.Label('StandardDialog Example')				# ������ǩ
		self.fixed.put(self.label1, 80, 40)						# ��ӱ�ǩ
		self.button1 = gtk.Button('FileChooser')						# ������ť
		self.button1.connect('clicked',self.OnButton1, 'FileChooser')			# �󶨰�ť�¼�
		self.button2 = gtk.Button('FontChooser')						# ������ť
		self.button2.connect('clicked',self.OnButton2, 'FontChooser')			# �󶨰�ť�¼�
		self.button3 = gtk.Button('ColorChooser')						# ������ť
		self.button3.connect('clicked',self.OnButton3, 'ColorChooser')			# �󶨰�ť�¼�
		self.fixed.put(self.button1, 10, 130)						# ��Ӱ�ť
		self.fixed.put(self.button2, 95, 130)						# ��Ӱ�ť
		self.fixed.put(self.button3, 190, 130)						# ��Ӱ�ť
		self.window.add(self.fixed)							# �򴰿������Fixed
		self.label1.show()								# ��ʾ���
		self.button1.show()
		self.button2.show()
		self.button3.show()
		self.fixed.show()
		self.window.show()
	def OnButton1(self, widget, data):							# ��ť�¼�������
		dialog = gtk.FileChooserDialog('Open',						# �����ļ��򿪶Ի���
                               None,								# ���ø�����
                               gtk.FILE_CHOOSER_ACTION_OPEN,					# ���öԻ����־
                               (gtk.STOCK_CANCEL, 						# ���Cancel��ť
				gtk.RESPONSE_CANCEL,						# Cancel��ť�ķ���ֵ
                                gtk.STOCK_OPEN, 						# ���Open��ť
				gtk.RESPONSE_OK))						# Open��ť�ķ���ֵ
		filter = gtk.FileFilter()							# ����gtk.FileFilter����
		filter.set_name('All files')							# ����ļ�������
		filter.add_pattern('*')								# �������ļ�
		dialog.add_filter(filter)							# ��Ի��������gtk.FileFilter����
		filter = gtk.FileFilter()							# ����gtk.FileFilter����
		filter.set_name('Python')							# ����ļ�������
		filter.add_pattern('*.py')							# ����ļ���׺��
		filter.add_pattern('*.pyw')							# ����ļ���׺��
		dialog.add_filter(filter)							# �򴰿������gtk.FileFilter����
		r = dialog.run()								# ��ʾ�Ի���
		if r == gtk.RESPONSE_OK:
			print dialog.get_filename()
		dialog.destroy()								# ���ٶԻ���
	def OnButton2(self, widget, data):							# ��ť�¼�������
		fontdlg = gtk.FontSelectionDialog('Choose Font')				# ��������ѡ�жԻ���
		r = fontdlg.run()								# ��ʾ�Ի���
		if r == gtk.RESPONSE_OK:
			print fontdlg.get_font_name()
		fontdlg.destroy()								# ���ٶԻ���
	def OnButton3(self, widget, data):							# ��ť�¼�������
            	colordlg = gtk.ColorSelectionDialog('Choose Color')				# ������ɫѡ��Ի���
		colordlg.colorsel.set_has_palette(True)						# ��ʾ��ɫ��
            	response = colordlg.run()							# ��ʾ�Ի���
            	if response == gtk.RESPONSE_OK:
            	    print colordlg.colorsel.get_current_color()
            	colordlg.destroy()								# ���ٶԻ���
	def main(self):										# ����main����
		gtk.main()
window = MyWindow('PyGTK', 300, 200)								# �������ڶ���
window.main()

