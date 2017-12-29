# -*- coding:utf-8 -*-
# file: wxPythonMenu.py
#
import wx											# ����wxPython
class MyApp(wx.App):										# ͨ���̳д�����
	def OnInit(self):									# ����OnInit����
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))		# ���ɿ�ܴ���
		panel = wx.Panel(frame, -1)							# �������
		menuBar = wx.MenuBar()								# �����˵���
		menu = wx.Menu()								# �����˵�
		open = menu.Append(-1, 'Open')							# ��˵������Open
		exit = menu.Append(-1, 'Save')							# ��˵������Save
		menu.AppendSeparator()								# ��˵�����ӷָ���
		close = menu.Append(-1, 'Close')						# ��˵������Close
		menuBar.Append(menu, '&File')							# ��˵��������File
		menu = wx.Menu()								# ���´����˵�
		copy = menu.Append(-1, 'Copy')							# ��˵������Copy
		paste = menu.Append(-1, 'Paste')						# ��˵������Paste
		cut = menu.Append(-1, 'Cut')							# ��˵������Cut 
		menu.AppendSeparator()								# ��˵�����ӷָ���
		selectall = menu.Append(-1, 'SelectAll')					# ��˵������SelectAll
		menuBar.Append(menu, '&Edit')							# ��˵��������Edit
		menu = wx.Menu()								# ���´����˵�
		about = menu.Append(-1, 'About')						# ��˵������About
		menuBar.Append(menu, '&Help')							# ��˵��������Help
		frame.SetMenuBar(menuBar)							# ���ܴ�������Ӳ˵�
		frame.Show()									# ��ʾ����
		return True
app = MyApp()
app.MainLoop()
