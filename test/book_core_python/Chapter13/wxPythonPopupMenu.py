# -*- coding:utf-8 -*-
# file: wxPythonPopupMenu.py
#
import wx											# ����wxPython
class MyApp(wx.App):										# ͨ���̳д�����
	def OnInit(self):									# ����OnInit����
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))		# ���ɿ�ܴ���
		self.panel = wx.Panel(frame, -1)						# �������
		menuBar = wx.MenuBar()								# �����˵���
		self.menu = wx.Menu()								# �����˵�
		open = self.menu.Append(-1, 'Open')
		save = self.menu.Append(-1, 'Save')
		self.menu.AppendSeparator()	
		close = self.menu.Append(-1, 'Close')
		menuBar.Append(self.menu, '&File')
		frame.SetMenuBar(menuBar)							# ���ܴ�������Ӳ˵�
		self.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick)					# ���Ҽ��¼�
		frame.Show()
		return True
	def OnRClick(self, event):
		pos = (event.GetX(),event.GetY())						# ������������
		self.panel.PopupMenu(self.menu, pos)						# ��ʾ�˵�
app = MyApp()
app.MainLoop()
