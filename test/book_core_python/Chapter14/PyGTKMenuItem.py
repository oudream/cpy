# -*- coding:utf-8 -*-
# file: PyGTKMenuItem.py
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
		close = gtk.MenuItem('Close')						# ����Close�˵�����
		close.show()								# ��ʾClose
		filemenu.append(open)							# ��˵������Open
		filemenu.append(close)							# ��˵������Close
        	file = gtk.MenuItem('_File')						# ����File�˵����»��߱�ʾ��ݼ�
		file.set_submenu(filemenu)						# ��File�˵������
        	file.show()								# ��ʾFile�˵�
		editmenu = gtk.Menu()							# �����˵�
		copy = gtk.MenuItem('Copy')						# ����Copy�˵�����
		copy.show()								# ��ʾCopy
		paste = gtk.MenuItem('Paste')						# ����Paste�˵�����
		paste.show()								# ��ʾPaste
		editmenu.append(copy)							# ��˵������Copy
		editmenu.append(paste)							# ��˵������Paste
		edit = gtk.MenuItem('_Edit')						# ����Edit�˵�
		edit.set_submenu(editmenu)						# ��Edit�˵��������
		edit.show()								# ��ʾEdit�˵�
        	menubar = gtk.MenuBar()							# ���ɲ˵���
		menubar.append(file)							# ��˵��������File�˵�
        	menubar.append(edit)							# ��˵��������Edit�˵�
		fixed.put(menubar, 0, 0)						# ��Fixed�������Ӳ˵���
        	menubar.show()								# ��ʾ�����
		fixed.show()
		window.show()
	def main(self):									# ����main����
		gtk.main()
window = MyWindow('PyGTK', 300, 200)							# �������ڶ���
window.main()
