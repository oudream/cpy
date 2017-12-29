# -*- coding:utf-8 -*-
# file: Dialog.py
#
import win32ui								# ����win32uiģ��
import win32con 							# ����win32conģ��
from pywin.mfc import dialog						# ��pywin.mfc����dialog
class MyDialog(dialog.Dialog):						# ���ضԻ����ʼ������
	def OnInitDialog(self):						# ���ø���ĶԻ����ʼ������
		dialog.Dialog.OnInitDialog(self)			# ����OnOK����
	def OnOK(self):							#
		win32ui.MessageBox('Press Ok',	\
				'Python',	\
				win32con.MB_OK)
		self.EndDialog(1)
	def OnCancel(self):						# ����OnCancel����
		win32ui.MessageBox('Press Cancel',\
				'Python',	  \
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
ButOK = (['Button',							# ����OK��ť����
	"OK",
	win32con.IDOK,
	(80,150, 50, 14), 
	buttonstyle | win32con.BS_PUSHBUTTON])
ButCancel = (['Button',							# ����Cancel��ť����
		"Cancel",
		win32con.IDCANCEL,
		(160, 150, 50, 14),
		buttonstyle | win32con.BS_PUSHBUTTON])
Stadic = (['Static',							# ���ñ�ǩ����
		'Python Dialog',
		12,
		(130,50,60,14),
		childstyle])
Edit = (['Edit',							# �����ı�������
		'',
		13,
		(130,80,60,14),
		childstyle|win32con.ES_LEFT|
		win32con.WS_BORDER|win32con.WS_TABSTOP])
init = []								# ��ʼ����Ϣ�б�
init.append(di)
init.append(ButOK)
init.append(ButCancel)
init.append(Stadic)
init.append(Edit)
mydialog = MyDialog(init)						# ���ɶԻ���ʵ������
mydialog.DoModal()							# �����Ի���

