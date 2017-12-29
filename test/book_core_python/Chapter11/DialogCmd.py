# -*- coding:utf-8 -*-
# file: DialogCmd.py
#
import win32ui								# ����win32uiģ��
import win32con 							# ����win32conģ��
from pywin.mfc import dialog						# ��pywin.mfc����dialog
class MyDialog(dialog.Dialog):						# ͨ���̳�dialog.Dialog���ɶԻ�����
	def OnInitDialog(self):						# ���ضԻ����ʼ������
		dialog.Dialog.OnInitDialog(self)			# ���ø���ĶԻ����ʼ������
		self.HookCommand(self.OnButton1,1051)			# ������Ϣ������ 
		self.HookCommand(self.OnButton2,1052) 
	def OnButton1(self,wParam,lParam):				# ����Button1�����Ϣ
		win32ui.MessageBox('Button1',	\
				'Python',	\
				win32con.MB_OK)
		self.EndDialog(1)
	def OnButton2(self,lParam,wParam):				# ����Button2�����Ϣ
		text = self.GetDlgItemText(1054)
		win32ui.MessageBox(text,	\
				'Python',	\
				win32con.MB_OK)
		self.EndDialog(1)
style = (win32con.DS_MODALFRAME  |					# ����Ի�����ʽ
	     win32con.WS_POPUP 	 |
	     win32con.WS_VISIBLE |
	     win32con.WS_CAPTION |
	     win32con.WS_SYSMENU |
	     win32con.DS_SETFONT)
childstyle = (win32con.WS_CHILD |					# ����ؼ���ʽ
	  win32con.WS_VISIBLE)
buttonstyle = win32con.WS_TABSTOP | childstyle				# ���尴ť��ʽ
di = ['Python',								# ���öԻ������� 
	(0,0,300,180),
	style,
	None,
	(8, "MS Sans Serif")]
Button1 = (['Button',							# ����OK��ť����
	'Button1',
	1051,
	(80,150, 50, 14), 
	buttonstyle | win32con.BS_PUSHBUTTON])
Button2 = (['Button',							# ����Cancel��ť����
	'Button2',
	1052,
	(160, 150, 50, 14),
	buttonstyle | win32con.BS_PUSHBUTTON])
Stadic = (['Static',							# ���ñ�ǩ����
	'Python Dialog',
	1053,
	(130,50,60,14),
	childstyle])
Edit = (['Edit',							# �����ı�������
	'',
	1054,
	(130,80,60,14),
	childstyle|win32con.ES_LEFT|
	win32con.WS_BORDER|win32con.WS_TABSTOP])
init = []								# ��ʼ����Ϣ�б�
init.append(di)
init.append(Button1)
init.append(Button2)
init.append(Stadic)
init.append(Edit)
mydialog = MyDialog(init)						# ���ɶԻ���ʵ������
mydialog.DoModal()							# �����Ի���



