# -*- coding:utf-8 -*-
# file: DllMenu.py
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
		dll = win32ui.LoadLibrary('Res.dll')				# ����DLL�ļ�
		m = win32ui.LoadMenu(7001,dll)					# ����˵�
		self._obj_.SetMenu(m)						# �򴴽���Ӳ˵�
	# ����OnClose����
	def OnClose(self):
		self.EndModalLoop(0)
	# ����OnPaint�������ڴ����������MFC GUI��
	def OnPaint(self):
		dc,ps = self.BeginPaint()
		dc.DrawText('MFC GUI',
			self.GetClientRect(),
			DT_SINGLELINE | DT_CENTER | DT_VCENTER)
		self.EndPaint(ps)

w = MyWnd()				# ���ɴ��ڶ���			
w.ShowWindow()				# ��ʾ����
w.UpdateWindow()			# ˢ�´���
w.RunModalLoop(1)			# ������Ϣѭ��
