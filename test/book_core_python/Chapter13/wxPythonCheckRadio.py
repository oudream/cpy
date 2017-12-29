# -*- coding:utf-8 -*-
# file: wxPythonCheckRadio.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# ���ɿ�ܴ���
		panel = wx.Panel(frame, -1)							# �������
		self.radio1 = wx.RadioButton(panel, 						# ���ɵ�ѡ��
				-1, 								# ָ����ѡ��ID
				'Radio1',							# ָ����ѡ���ı�
				pos=(10, 40),							# ָ����ѡ��λ��
				style=wx.RB_GROUP)						# ָ����ѡ����ʽ
		self.radio2 = wx.RadioButton(panel,						# ���ɿ�ܴ���
				-1, 								# ָ����ѡ��ID
				'Radio2',							# ָ����ѡ���ı�
				pos=(10, 80))							# ָ����ѡ��λ��
		self.radio3 = wx.RadioButton(panel, 						# ���ɵ�ѡ��
				-1, 								# ָ����ѡ��ID
				'Radio3', 							# ָ����ѡ���ı�
				pos=(10, 120))							# ָ����ѡ��λ��
		self.check = wx.CheckBox(panel, 						# ���ɸ���ѡ��
				-1, 								# ָ������ѡ��ID
				'CheckBox',							# ָ������ѡ���ı�
				pos = (120, 40),						# ָ����ѡ��λ��
				size = (150, 20))						# ָ����ѡ���С
		self.button1 = wx.Button(panel,-1,'Radio',pos = (120,80))			# ���ɰ�ť
		self.button2 = wx.Button(panel,-1,'Check',pos = (120,120))
		self.Bind(wx.EVT_BUTTON, self.OnButton1, self.button1)				# �󶨰�ť�¼�
		self.Bind(wx.EVT_BUTTON, self.OnButton2, self.button2)
		frame.Show()
		return True
	def OnButton1(self, event):								# ��ť�¼�������
		if self.radio1.GetValue():							# �ж�Radio1�Ƿ�ѡ��
			self.button1.SetLabel('Radio1')
		elif self.radio2.GetValue():							# �ж�Radio2�Ƿ�ѡ��
			self.button1.SetLabel('Radio2')
		else:
			self.button1.SetLabel('Radio3')
	def OnButton2(self, event):								# ��ť�¼�������
		if self.check.IsChecked():							# �ж�CheckBox�Ƿ�ѡ��
			self.button2.SetLabel('Checked')
		else:
			self.button2.SetLabel('UnChecke')
app = MyApp()
app.MainLoop()
