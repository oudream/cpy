# -*- coding:utf-8 -*-
# file: SimpleDialog.py
#
import win32ui							# ����Win32uiģ��
import win32con							# ����win32conģ�� 
from pywin.mfc import dialog					# ����pywin.mfc�е�dialogģ��
class MyDialog(dialog.Dialog):					# ͨ���̳�dialog.Dialog���ɶԻ�����
	def OnInitDialog(self):					# ���س�ʼ������
		dialog.Dialog.OnInitDialog(self)		# ���ø���ĳ�ʼ������
style = (win32con.DS_MODALFRAME  |
	     win32con.WS_POPUP 	 |
	     win32con.WS_VISIBLE |
	     win32con.WS_CAPTION |
	     win32con.WS_SYSMENU |
	     win32con.DS_SETFONT)
di = ['Python',							# ���öԻ������ԣ����ñ���Ϊ��Python��
	(0,0,300,180),						# ���öԻ���λ�ü���С
	style,							# ���öԻ�����ʽ
	None,							# ���öԻ�����չ��ʽ
	(8, "MS Sans Serif")]					# ���öԻ������弰��С
init = []							# ����Ի����ʼ�������б�
init.append(di) 
mydialog = MyDialog(init)					# ���ɶԻ���ʵ������
mydialog.DoModal()						# ��ʾ�Ի���	
