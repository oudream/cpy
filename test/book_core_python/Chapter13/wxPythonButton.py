# -*- coding:utf-8 -*-
# file: wxPythonButton.py
#
import wx									# ����wxPython
class MyApp(wx.App):								# ͨ���̳д�����
	def OnInit(self):							# ����OnInit����
		frame = wx.Frame(parent = None,title = 'Button')		# ���ɿ�ܴ���
		panel = wx.Panel(frame, -1)					# �������
		button = wx.Button(panel,					# �������Ӱ�ť
				-1,						# ָ����ťID
				'Button',					# ָ����ť�ϵ��ı�
				pos=(50,50))					# ָ����ť������ϵ�λ��
		frame.Show()							# ��ʾ����
		return True
app = MyApp()									# ��ʵ����
app.MainLoop()									# ������Ϣѭ��
