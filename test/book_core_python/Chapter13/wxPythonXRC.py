# -*- coding:utf-8 -*-
# file: wxPythonXRC.py
#
import wx
from wx import xrc
class MyApp(wx.App):
	def OnInit(self):
		self.res = xrc.XmlResource('res.xrc')						# ������Դ�ļ�
		self.frame = self.res.LoadFrame(None, 'frame')					# ����Դ�ļ�������frame
		self.panel = xrc.XRCCTRL(self.frame, 'panel')					# ����panel
		self.label = xrc.XRCCTRL(self.panel, 'label')					# ����label
		self.text = xrc.XRCCTRL(self.panel, 'text')					# ����text
		self.button = xrc.XRCCTRL(self.panel, 'button')					# ����button
		self.Bind(wx.EVT_BUTTON, self.OnButton, self.button)				# �󶨰�ť�¼�
		self.frame.Show()
		return True
	def OnButton(self, event):								# ����ť�¼�
		wx.MessageBox('You input:'+self.text.GetValue(), 'wxPython', wx.OK)
app = MyApp(False)
app.MainLoop()
