# -*- coding:utf-8 -*-
# file: wxPythonSizer.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# ���ɿ�ܴ���
		panel = wx.Panel(frame, -1)							# �������
		sizer = wx.GridSizer(rows=3, cols=3)						# ����һ���������е�sizer
		sizer.AddSpacer(0)								# ��sizer�����һ������
		label = wx.StaticText(panel, -1, 'label')					# ���ɱ�ǩ
		sizer.Add(label,flag = wx.ALIGN_CENTER)						# ��sizer��ӱ�ǩ���ж���
		sizer.AddSpacer(0)	
		button1 = wx.Button(panel, -1, 'Button1')					# ���ɰ�ť
		sizer.Add(button1,flag = wx.ALIGN_CENTER)					# ��sizer����Ӱ�ť
		sizer.AddSpacer(0)
		button2 = wx.Button(panel, -1, 'Button2')					# ���ɰ�ť
		sizer.Add(button2,flag = wx.ALIGN_CENTER)					# ��sizer����Ӱ�ť
		sizer.AddSpacer(0)
		text = wx.TextCtrl(panel, -1, size = (100,20))					# �����ı���
		sizer.Add(text)									# ��sizer������ı���
		sizer.AddSpacer(0)
		panel.SetSizer(sizer)								# ����������sizer
		frame.Show()
		return True
app = MyApp()
app.MainLoop()
