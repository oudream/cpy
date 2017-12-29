# -*- coding:utf-8 -*-
# file: PyMenuEvent.py
#
import pygtk										# ����pygtkģ��
pygtk.require('2.0')									# ����pygtk�����gtk�汾
import gtk										# ����gtkģ��
class MyWindow():									# ���崰����
	def __init__(self, title, width, height):					# �����ʼ������
		window = gtk.Window()							# ���ɴ��ڶ���
		window.set_title(title)							# ���ô��ڱ���
		window.set_default_size(width, height)					# ���ô��ڴ�С
		window.connect('destroy', lambda q: gtk.main_quit())			# �رմ����˳�����
		fixed = gtk.Fixed()							# ����Fixed���
		window.add(fixed)
		filemenu = gtk.Menu()							# �����˵�
		open = gtk.MenuItem('Open')						# ����Open�˵�����
		open.show()								# ��ʾOpen
		open.connect('activate', self.OnOpen, 'Open')				# �󶨲˵��¼�
		close = gtk.MenuItem('Close')						# ����Close�˵�����
		close.connect('activate', self.OnClose, 'Close')			# �󶨲˵��¼�
		close.show()								# ��ʾClose
		filemenu.append(open)							# ��˵������Open
		filemenu.append(close)							# ��˵������Close
        	file = gtk.MenuItem('_File')						# ����File�˵����»��߱�ʾ��ݼ�
		file.set_submenu(filemenu)						# ��File�˵������
        	file.show()								# ��ʾFile�˵�
        	menubar = gtk.MenuBar()							# ���ɲ˵���
		menubar.append(file)							# ��˵��������File�˵�
		fixed.put(menubar, 0, 0)						# ��Fixed�������Ӳ˵���
        	menubar.show()								# ��ʾ�����
		fixed.show()
		window.show()
	def OnOpen(self, widget, data):							# ����˵��¼�
		dialog = gtk.FileChooserDialog('Open',					# �������ļ��Ի���
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)
		response = dialog.run()
		dialog.destroy()
	def OnClose(self, widget, data):						# ����˵��¼�
		gtk.main_quit()								# �˳�����
	def main(self):									# ����main����
		gtk.main()
window = MyWindow('PyGTK', 300, 200)							# �������ڶ���
window.main()
