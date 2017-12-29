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
		# ���˵���ӵ�������
		self._obj_.SetMenu(menu)
		# ���ò˵�������Ϣ
		self.HookCommand(self.MenuClick,1051)
		self.HookCommand(self.MenuClick,1052)
		self.HookCommand(self.MenuClick,1053)
		# ����OnClose����
	def OnClose(self):
		self.EndModalLoop(0)
	def MenuClick(self,lParam,wParam):
		# ����lParam�����жϵ���Ĳ˵�
		if lParam == 1051:
			self.MessageBox('Open','Python',MB_OK)
		elif lParam == 1053:
			self.MessageBox('Save','Python',MB_OK)
		else:
			self.OnClose()
w = MyWnd()											# ���ɴ��ڶ���
w.ShowWindow()											# ��ʾ����
w.UpdateWindow()										# ˢ�´���
w.RunModalLoop(1)										# ������Ϣѭ��


