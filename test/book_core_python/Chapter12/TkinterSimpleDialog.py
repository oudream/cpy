# -*- coding:utf-8 -*-
# file: TkinterSimpleDialog.py
#
import Tkinter										# ����Tkinterģ��
import tkSimpleDialog									# ����tkSimpleDialogģ��
def InStr():										# ��ť�¼�������
	r = tkSimpleDialog.askstring('Python Tkinter',					# �����ַ�������Ի���
			'Input String',							# ָ����ʾ�ַ�
			initialvalue='Tkinter')						# ָ����ʼ���ı�
	print r										# �������ֵ
def InInt():										# ��ť�¼�������
	r = tkSimpleDialog.askinteger('Python Tkinter','Input Integer')			# ������������Ի���
	print r
def InFlo():										# ��ť�¼�������
	r = tkSimpleDialog.askfloat('Python Tkinter','Input Float')			# ��������������Ի���
	print r
root = Tkinter.Tk()
button1 = Tkinter.Button(root,text = 'Input String',					# ������ť
		command = InStr)							# ָ����ť�¼�������
button1.pack(side='left')
button2 = Tkinter.Button(root,text = 'Input Integer',
		command = InInt)							# ָ����ť�¼�������
button2.pack(side='left')
button2 = Tkinter.Button(root,text = 'Input Float',
		command = InFlo)							# ָ����ť�¼�������
button2.pack(side='left')
root.mainloop()										# ������Ϣѭ��
