# -*- coding:utf-8 -*-
# file: PyGTKMenu.py
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
		menu_items = (								# �˵�
       			     ( '/_File',      None,         None, 0, '<Branch>' ),
       			     ( '/File/Open',  '<control>O', None, 0, None ),
       			     ( '/File/Save',  '<control>S', None, 0, None ),
       			     ( '/File/s',  None,         None, 0, '<Separator>' ),
       			     ( '/File/Close', '<control>Q', None, 0, None ),
       			     ( '/_Edit',      None,         None, 0, '<Branch>' ),
       			     ( '/Edit/Copy',  None,         None, 0, None ),
			     ( '/Edit/Paste',  None,         None, 0, None ),
			     ( '/Edit/s',  None,         None, 0, '<Separator>' ),
			     ( '/Edit/Cut',  None,         None, 0, None ),
       			     ( '/_Help',      None,         None, 0, '<Branch>' ),
       			     ( '/Help/About', None,         None, 0, None ),
       			     )
		accel_group = gtk.AccelGroup()						# ������ݼ�����
		itemfactory = gtk.ItemFactory(gtk.MenuBar, '<main>', accel_group)	# ����ItemFactory����
        	itemfactory.create_items(menu_items)					# �Ӳ˵�Ԫ�鴴���˵�
        	window.add_accel_group(accel_group)					# �򴰿�����ӿ�ݼ�
        	menubar = gtk.MenuBar()							# ���ɲ˵���
		menubar = itemfactory.get_widget('<main>')				# ��ò˵��˵�
		fixed.put(menubar, 0, 0)						# ��Fixed�������Ӳ˵���
        	menubar.show()								# ��ʾ�����
		fixed.show()
		window.show()
	def main(self):									# ����main����
		gtk.main()
window = MyWindow('PyGTK', 300, 200)							# �������ڶ���
window.main()
