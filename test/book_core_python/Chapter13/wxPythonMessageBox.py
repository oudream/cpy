# -*- coding:utf-8 -*-
# file: wxPythonMessageBox.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		self.frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# 生成框架窗口
		panel = wx.Panel(self.frame, -1)							# 生成面板
		self.button1 = wx.Button(panel,-1,'Style1',pos = (100,20))				# 生成按钮
		self.button2 = wx.Button(panel,-1,'Style2',pos = (100,50))
		self.button3 = wx.Button(panel,-1,'Style3',pos = (100,80))
		self.button4 = wx.Button(panel,-1,'Style4',pos = (100,110))
		self.button5 = wx.Button(panel,-1,'Style5',pos = (100,140))
		self.Bind(wx.EVT_BUTTON, self.OnButton1, self.button1)					# 绑定按钮事件
		self.Bind(wx.EVT_BUTTON, self.OnButton2, self.button2)
		self.Bind(wx.EVT_BUTTON, self.OnButton3, self.button3)
		self.Bind(wx.EVT_BUTTON, self.OnButton4, self.button4)
		self.Bind(wx.EVT_BUTTON, self.OnButton5, self.button5)
		self.frame.Show()
		return True
	def OnButton1(self, event):									# 按钮事件处理方法
		wx.MessageBox('Style1', 'wxPython',							# 创建MessageBox
			wx.YES_NO | wx.ICON_QUESTION)
	def OnButton2(self, event):									# 按钮事件处理方法
		wx.MessageBox('Sytle2','wxPython',							# 创建MessageBox
			wx.OK|wx.CANCEL|wx.ICON_ERROR)
	def OnButton3(self, event):									# 按钮事件处理方法
		wx.MessageBox('Style3', 'wxPython',							# 创建MessageBox
			wx.OK|wx.CANCEL | wx.ICON_EXCLAMATION)
	def OnButton4(self, event):									# 按钮事件处理方法
		wx.MessageBox('Style4', 'wxPython',							# 创建MessageBox
			wx.YES_NO|wx.NO_DEFAULT | wx.ICON_HAND)
	def OnButton5(self, event):									# 按钮事件处理方法
		wx.MessageBox('Style5', 'wxPython',							# 创建MessageBox
			wx.YES_NO|wx.YES_DEFAULT | wx.ICON_INFORMATION)
app = MyApp()
app.MainLoop()
