# -*- coding:utf-8 -*-
# file: wxPythonDialog.py
#
import wx											# ����wxPython
class MyApp(wx.App):										# ͨ���̳д�����
	def OnInit(self):									# ����OnInit����
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))		# ���ɿ�ܴ���
		panel = wx.Panel(frame, -1)							# �������
		self.button = wx.Button(panel, -1, 'Show Dialog', pos=(100, 50))		# ���Button
		self.Bind(wx.EVT_BUTTON, self.OnButton, self.button)
		frame.Show()									# ��ʾ����
		return True
	def OnButton(self, event):								# ��ť�¼���Ӧ����
		dialog = MyDialog()
		r = dialog.ShowModal()								# ��ȡ����ֵ
		if r == wx.ID_OK:								# �ж��Ƿ񵥻��Ի����Ok��ť
			wx.MessageBox('You input:' + dialog.text.GetValue(),			# ������Ϣ��
					'wxPython', wx.OK)
		dialog.Destroy()								# ���ٶԻ���
class MyDialog(wx.Dialog):									# ����Ի�����
	def __init__(self):									# ��ʼ��
		wx.Dialog.__init__(self, None, -1, 'wxDilog',size=(300, 170))			# ���ø���ĳ�ʼ������
		label = wx.StaticText(self, -1, 'Simple Dialog',pos = (120,20))			# ���ɱ�ǩ
		self.text = wx.TextCtrl(self, -1, pos = (100,50), size = (160, -1))		# �����ı���
		self.ok = wx.Button(self, wx.ID_OK, "OK", pos=(50, 80))				# ����OK��ť	
		self.cancel = wx.Button(self, wx.ID_CANCEL, "Cancel",pos=(200, 80))		# ����Cancel��ť
app = MyApp()
app.MainLoop()
