# -*- coding:utf-8 -*-
# file: PopupMenu.py
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
		self.HookMessage(self.OnRClick,WM_RBUTTONDOWN)
	# ����OnClose����
	def OnClose(self):
		self.EndModalLoop(0)
	# ����������Ҽ���Ϣ
	def OnRClick(self, param):
		submenu = win32ui.CreatePopupMenu()
		submenu.AppendMenu(MF_STRING,1054,'Copy')				# ��˵������Copy
		submenu.AppendMenu(MF_STRING,1055,'Paste')				# ��˵������Paste
		submenu.AppendMenu(MF_SEPARATOR,1056,None)				# ��˵�����ӷָ���
		submenu.AppendMenu(MF_STRING,1057,'Cut')				# ��˵������Cut
		flag = TPM_LEFTALIGN|TPM_LEFTBUTTON|TPM_RIGHTBUTTON 			# ����ʽ�˵���ʽ
		submenu.TrackPopupMenu(param[5],flag,self)				# paramΪϵͳ��OnRClick�������ݵĲ�������Ϊһ��Ԫ�飬���6��Ϊ���x��y������ɵ�Ԫ��
w = MyWnd()				# ���ɴ��ڶ���			
w.ShowWindow()				# ��ʾ����
w.UpdateWindow()			# ˢ�´���
w.RunModalLoop(1)			# ������Ϣѭ��
