# -*- coding:utf-8 -*-
# file: UseMenu.py
#
import win32ui
import win32api
from win32con import *
from pywin.mfc import window
# ���崰����
class MyWnd(window.Wnd):
	def __init__ (self):
		window.Wnd.__init__(self, win32ui.CreateWnd ())
	 	self._obj_.CreateWindowEx(WS_EX_CLIENTEDGE, \
           		win32ui.RegisterWndClass(0, 0, COLOR_WINDOW + 1), \
            		'MFC GUI', WS_OVERLAPPEDWINDOW, \
            		(10, 10, 800, 500), None, 0, None)
		# �����˵�����
		submenu = win32ui.CreateMenu()
		menu = win32ui.CreateMenu()
		# ��˵������Open������&��ʾ����ʹ��Alt+&�����ĸ���ʸò˵�����
		submenu.AppendMenu(MF_STRING,1051,'&Open')	
		# ��˵������Close
		submenu.AppendMenu(MF_STRING,1052,'&Close')	
		# ��˵������Save
		submenu.AppendMenu(MF_STRING,1053,'&Save')
		# ������Ĳ˵���ӵ�File�˵���
		menu.AppendMenu(MF_STRING|MF_POPUP,submenu.GetHandle(),'&File')
		submenu = win32ui.CreateMenu()
		# ��˵������Copy
		submenu.AppendMenu(MF_STRING,1054,'&Copy')
		# ��˵������Paste
		submenu.AppendMenu(MF_STRING,1055,'&Paste')	
		# ��˵�����ӷָ���
		submenu.AppendMenu(MF_SEPARATOR,1056,None)
		# ��˵������Cut
		submenu.AppendMenu(MF_STRING,1057,'C&ut')
		# ������Ĳ˵���ӵ�Edit�˵���
		menu.AppendMenu(MF_STRING|MF_POPUP,submenu.GetHandle(),'&Edit')
		submenu = win32ui.CreateMenu()
		# ��˵������Tools
		submenu.AppendMenu(MF_STRING,1058,'Tools')
		# ��˵������Settings
		submenu.AppendMenu(MF_STRING|MF_GRAYED,1059,'Setting')
		m = win32ui.CreateMenu()
		# ������Ĳ˵���ӵ�Option�˵���
		m.AppendMenu(MF_STRING|MF_POPUP|MF_CHECKED,submenu.GetHandle(),'Option')
		# ��Option�˵���ӵ�Other�˵���
		menu.AppendMenu(MF_STRING|MF_POPUP,m.GetHandle(),'&Other')
		# ���˵���ӵ�������
		self._obj_.SetMenu(menu)
	# ����OnClose����
	def OnClose(self):
		self.EndModalLoop(0)
w = MyWnd()											# ���ɴ��ڶ���
w.ShowWindow()											# ��ʾ����
w.UpdateWindow()										# ˢ�´���
w.RunModalLoop(1)										# ������Ϣѭ��

