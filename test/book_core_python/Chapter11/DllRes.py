# -*- coding:utf-8 -*-
# file: DllRes.py
#
import win32ui							# ����Win32uiģ��
import win32con							# ����win32conģ�� 
from pywin.mfc import dialog					# ����pywin.mfc�е�dialogģ��
class MyDialog(dialog.Dialog):					# ͨ���̳�dialog.Dialog���ɶԻ�����
	def OnInitDialog(self):					# ���س�ʼ������
		dialog.Dialog.OnInitDialog(self)		# ���ø���ĳ�ʼ������
	def OnOK(self):						# ����OnOK����
		win32ui.MessageBox('Press Ok',	\
				'Python',	\
				win32con.MB_OK)	
		self.EndDialog(1)
	def OnCancel(self):					# ����OnCancel����
		win32ui.MessageBox('Press Cancel',\
				'Python',	  \
				win32con.MB_OK)
		self.EndDialog(1)	
dll = win32ui.LoadLibrary('Res.dll')
l = win32ui.LoadDialogResource(7000,dll)
mydialog = MyDialog(l)						# ���ɶԻ���ʵ������
mydialog.DoModal()						# ��ʾ�Ի���	
