# -*- coding:utf-8 -*-
# file: wxPythonButtonEvent.py
#
import wx											# ����wxPython
class MyApp(wx.App):										# ͨ���̳д�����
	def OnInit(self):									# ����OnInit����
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))		# ���ɿ�ܴ���
		panel = wx.Panel(frame, -1)							# �������
		self.button1 = wx.Button(panel, -1, 'Button1', pos=(50, 50))			# ���Button1
		self.Bind(wx.EVT_BUTTON, 							# �󶨰�ť�¼�
			self.OnButton1, 							# ָ���¼���Ӧ����
			self.button1)								# ָ����ť
		self.button2 = wx.Button(panel, -1, 'Button2',pos = (150,50))
		self.Bind(wx.EVT_BUTTON,							# �󶨰�ť�¼� 
			self.OnButton2,                                                         # ָ���¼���Ӧ����
			self.button2)								# ָ����ť
		self.button1.SetDefault()							# ��Button1����ΪĬ�ϰ�ť
		frame.Show()									# ��ʾ����
		return True
	def OnButton1(self, event):								# ��ť�¼���Ӧ����
		self.button2.SetLabel('Button1')						# ����Button2������
		self.button2.SetDefault()							# ��Button2����ΪĬ�ϰ�ť
		self.button1.SetLabel('Button2')						# ����Button1������
	def OnButton2(self, event):								# ��ť�¼���Ӧ����
		self.button1.SetLabel('Button1')						# ����Button1������
		self.button1.SetDefault()							# ��Button1����ΪĬ�ϰ�ť
		self.button2.SetLabel('Button2')						# ����Button2������
app = MyApp()
app.MainLoop()
