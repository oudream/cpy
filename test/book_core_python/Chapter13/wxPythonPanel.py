# -*- coding:utf-8 -*-
# file: wxPythonPanel.py
#
import wx								# ����wxPythonģ��
class MyApp(wx.App):							# ͨ���̳�wx.App�ഴ����
	def OnInit(self):						# ����OnInit����
		frame = wx.Frame(parent = None,				# ������ܴ���
				id=-1, 					# ָ�����ID
				title='Panel', 				# ָ�����ڱ���
				pos=(100,100),				# ָ������λ��
				size=(600,480), 			# ָ�����ڴ�С
				style=wx.DEFAULT_FRAME_STYLE,		# ָ��������ʽ
				name="frame")				# ָ��������
		panel = wx.Panel(frame, -1)				# ���ܴ���������
		frame.Show()						# ��ʾ��ܴ���
		return True						# ����True
app = MyApp()								# ��ʵ����
app.MainLoop()								# ������Ϣѭ��
