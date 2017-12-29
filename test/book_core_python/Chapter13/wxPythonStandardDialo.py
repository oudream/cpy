# -*- coding:utf-8 -*-
# file: wxPythonStandardDialog.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		self.frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# ���ɿ�ܴ���
		panel = wx.Panel(self.frame, -1)							# �������
		self.button1 = wx.Button(panel,-1,'Input String',pos = (100,20))			# ���ɰ�ť
		self.button2 = wx.Button(panel,-1,'Input Password',pos = (100,70))
		self.button3 = wx.Button(panel,-1,'Input Number',pos = (100,120))
		self.Bind(wx.EVT_BUTTON, self.OnButton1, self.button1)					# �󶨰�ť�¼�
		self.Bind(wx.EVT_BUTTON, self.OnButton2, self.button2)
		self.Bind(wx.EVT_BUTTON, self.OnButton3, self.button3)
		self.frame.Show()
		return True
	def OnButton1(self, event):
		r = wx.GetTextFromUser('wxPython','String', 'Default')					# �����ı������
		wx.MessageBox(r, 'wxPython',wx.OK)							# ����MessageBox
	def OnButton2(self, event):
		r = wx.GetPasswordFromUser('wxPython','Password')					# �������������
		wx.MessageBox(r, 'wxPython',wx.OK)							# ����MessageBox
	def OnButton3(self, event):
		r = wx.GetNumberFromUser('Input Number','Number','wxPython',80)				# �������������
		wx.MessageBox(str(r), 'wxPython',wx.OK)							# ����MessageBox
app = MyApp()
app.MainLoop()
