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
		submenu = win32ui.CreateMenu()						# �����˵�����
		menu = win32ui.CreateMenu()
		submenu.AppendMenu(MF_STRING,1051,'&Open')				# ��˵������Open������&��ʾ����ʹ��Alt+&�����ĸ���ʸò˵�����
		submenu.AppendMenu(MF_STRING,1052,'&Close')				# ��˵������Close
		submenu.AppendMenu(MF_STRING,1053,'&Save')				# ��˵������Save
		menu.AppendMenu(MF_STRING|MF_POPUP,submenu.GetHandle(),'&File')		# ������Ĳ˵���ӵ�File�˵���
		submenu = win32ui.CreateMenu()
		submenu.AppendMenu(MF_STRING,1054,'&Copy')				# ��˵������Copy
		submenu.AppendMenu(MF_STRING,1055,'&Paste')				# ��˵������Paste
		submenu.AppendMenu(MF_SEPARATOR,1056,None)				# ��˵�����ӷָ���
		submenu.AppendMenu(MF_STRING,1057,'C&ut')				# ��˵������Cut
		menu.AppendMenu(MF_STRING|MF_POPUP,submenu.GetHandle(),'&Edit')		# ������Ĳ˵���ӵ�Edit�˵���
		submenu = win32ui.CreateMenu()
		submenu.AppendMenu(MF_STRING,1058,'Tools')				# ��˵������Tools
		submenu.AppendMenu(MF_STRING|MF_GRAYED,1059,'Setting')			# ��˵������Settings
		m = win32ui.CreateMenu()
		m.AppendMenu(MF_STRING|MF_POPUP|MF_CHECKED,submenu.GetHandle(),'Option')# ������Ĳ˵���ӵ�Option�˵���
		menu.AppendMenu(MF_STRING|MF_POPUP,m.GetHandle(),'&Other')		# ��Option�˵���ӵ�Other�˵���
		self._obj_.SetMenu(menu)						# ���˵���ӵ�������
		self.HookMessage(self.OnRClick,WM_RBUTTONDOWN)
	# ����OnClose����
	def OnClose(self):
		self.EndModalLoop(0)
	def OnRClick(self, l):
		submenu = win32ui.CreatePopupMenu()
		#win32con.MF_STRING|win32con.MF_ENABLED|win32con.MF_POPUP
		submenu.AppendMenu(MF_STRING|MF_ENABLED|MF_POPUP,1054,'Copy')				# ��˵������Copy
		submenu.AppendMenu(MF_STRING|MF_POPUP,1055,'Paste')				# ��˵������Paste
		#submenu.AppendMenu(MF_SEPARATOR,1056,None)				# ��˵�����ӷָ���
		submenu.AppendMenu(MF_STRING,1057,'Cut')				# ��˵������Cut
		flag = TPM_LEFTALIGN|TPM_LEFTBUTTON|TPM_RIGHTBUTTON 
		submenu.TrackPopupMenu(l[5],flag,self)
	
w = MyWnd()				# ���ɴ��ڶ���			
w.ShowWindow()				# ��ʾ����
w.UpdateWindow()			# ˢ�´���
w.RunModalLoop(1)			# ������Ϣѭ��
