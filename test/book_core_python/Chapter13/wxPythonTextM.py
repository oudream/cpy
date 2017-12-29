# -*- coding:utf-8 -*-
# file: wxPythonTextM.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (600,400))		# ���ɿ�ܴ���
		panel = wx.Panel(frame, -1)							# �������
		label1 = wx.StaticText(panel, -1, 'MultiLine', pos = (280,10))			# ���ɱ�ǩ
		text1 = wx.TextCtrl(panel,							# �����ı���
				-1,  								# ָ���ı���ID
				pos = (10,30),							# ָ���ı���λ��
				size = (580, 150),style=wx.TE_MULTILINE)			# ָ���ı����С
		label2 = wx.StaticText(panel, -1, 'RichText', pos = (280,190))			# ���ɱ�ǩ
		text2 = wx.TextCtrl(panel,							# �����ı���
				-1,                                                             # ָ���ı���ID
				'Python wxPython',                                              # ָ����ʼ�ı�
				pos = (10,210),							# ָ���ı���λ��
				size = (580, 150),						# ָ���ı����С
				style =wx.TE_MULTILINE|wx.TE_RICH)				# ָ���ı���Ϊ�����
		text2.SetStyle(0, 6, wx.TextAttr('red', 'blue'))
		frame.Show()
		return True
app = MyApp()
app.MainLoop()
