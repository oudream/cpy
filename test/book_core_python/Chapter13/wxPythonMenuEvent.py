# -*- coding:utf-8 -*-
# file: wxPythonMenuEvent.py
#
import wx											# ����wxPython
class MyApp(wx.App):										# ͨ���̳д�����
	def OnInit(self):									# ����OnInit����
		self.frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))	# ���ɿ�ܴ���
		self.panel = wx.Panel(self.frame, -1)						# �������
		menuBar = wx.MenuBar()								# �����˵���
		self.menu = wx.Menu()								# �����˵�
		open = self.menu.Append(-1, 'Open')
		save = self.menu.Append(-1, 'Save')
		self.menu.AppendSeparator()	
		close = self.menu.Append(-1, 'Close')
		menuBar.Append(self.menu, '&File')
		self.menu = wx.Menu()								# ���´����˵�
		about = self.menu.Append(-1, 'About')
		menuBar.Append(self.menu, '&Help')
		self.frame.SetMenuBar(menuBar)							# ���ܴ�������Ӳ˵�
		self.Bind(wx.EVT_MENU, self.OnOpen, open)					# �󶨲˵��¼�
		self.Bind(wx.EVT_MENU, self.OnSave, save)
		self.Bind(wx.EVT_MENU, self.OnClose, close)
		self.Bind(wx.EVT_MENU, self.OnAbout, about)
		self.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick)
		self.frame.Show()
		return True
	def OnOpen(self, event):								# ����Open����
		dialog = wx.FileDialog(None, 'wxPython', style = wx.OPEN) 			# �������ļ��Ի���
		dialog.ShowModal()
		dialog.Destroy()
	def OnSave(self, event):								# ����Save����
		dialog = wx.FileDialog(None, 'wxPython', style =  wx.SAVE)			# ���������ļ��Ի���
		dialog.ShowModal()
		dialog.Destroy()
	def OnClose(self, event):								# ����Close����
		self.frame.Destroy()								# �˳�����
	def OnAbout(self, event):								# ����About����
		wx.MessageBox('wxPython Menu Event', 'wxPython', wx.OK)				# ������Ϣ��
	def OnRClick(self, event):								# �����Ҽ��¼�
		pos = (event.GetX(),event.GetY())
		self.panel.PopupMenu(self.menu, pos)						# ��������ʽ�˵�
app = MyApp()
app.MainLoop()
