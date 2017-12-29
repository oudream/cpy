# -*- coding:utf-8 -*-
# file: wxPythonStatic.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# ���ɿ�ܴ���
		panel = wx.Panel(frame, -1)							# �������
		label1 = wx.StaticText(panel,							# ���ɱ�ǩ
				-1, 								# ָ����ǩID
				'Python', 							# ָ����ǩ���ı�
				size = (160,20),						# ָ����ǩ��С
				pos = (60,10),							# ָ����ǩλ��
				style = wx.ALIGN_RIGHT)						# ָ����ǩ��ʽ���Ҷ���
		label2 = wx.StaticText(panel,							# ���ɱ�ǩ
				-1, 								# ָ����ǩID
				'Python',							# ָ����ǩ���ı�
				size = (160,20),						# ָ����ǩ��С
				pos = (60,50),							# ָ����ǩλ��
				style = wx.ALIGN_CENTER)					# ָ����ǩ��ʽ�����ж���
		label2.SetForegroundColour('red')						# ָ����ǩǰ��ɫ
		label2.SetBackgroundColour('black')						# ָ����ǩ����ɫ
		label3 = wx.StaticText(panel,							# ���ɱ�ǩ
				-1, 								# ָ����ǩID
				'Python\nwxPython',						# ���ı���ʹ�û��з�
				size = (160,40),						# ָ����ǩ��С
				pos = (60,90))							# ָ����ǩλ��
		frame.Show()
		return True
app = MyApp()
app.MainLoop()
