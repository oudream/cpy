# -*- coding:utf-8 -*-
# file: wxPythonTextS.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# ���ɿ�ܴ���
		panel = wx.Panel(frame, -1)							# �������
		label1 = wx.StaticText(panel, -1, 'wxPython', pos = (120,20))			# ���ɱ�ǩ
		label2 = wx.StaticText(panel, -1, 'User Name:',pos = (10,50)) 			# ���ɱ�ǩ
		text = wx.TextCtrl(panel,							# �����ı���
				-1,  								# ָ���ı���ID
				pos = (100,50),							# ָ���ı���λ��
				size = (160, -1))						# ָ���ı����С
		label3 = wx.StaticText(panel, -1, "Password:",pos = (10,100))			# ���ɱ�ǩ
		password = wx.TextCtrl(panel,							# �����ı���
				-1,                                                             # ָ���ı���ID
				"password",                                                     # ָ����ʼ�ı�
				pos = (100,100),						# ָ���ı���λ��
				size = (160, -1),						# ָ���ı����С
				style=wx.TE_PASSWORD)						# ָ���ı���Ϊ�����
		frame.Show()
		return True
app = MyApp()
app.MainLoop()

