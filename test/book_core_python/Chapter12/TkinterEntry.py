# -*- coding:utf-8 -*-
# file: TkinterEntry.py
#
import Tkinter								# ����Tkinterģ��
root = Tkinter.Tk()
entry1 = Tkinter.Entry(root,						# ���ɵ����ı������
			show = '*',)					# �����ı����е��ַ�����ʾΪ��*��
entry1.pack()								# ���ı�����ӵ�������
entry2 = Tkinter.Entry(root,
			show = '#',					# �����ı����е��ַ�����ʾΪ��#��
			width = 50)					# ���ı���Ŀ������Ϊ50
entry2.pack()
entry3 = Tkinter.Entry(root,
			bg = 'red',					# ���ı���ı���ɫ����Ϊ��ɫ
			fg = 'blue')					# ���ı����ǰ��ɫ����Ϊ��ɫ
entry3.pack()
entry4 = Tkinter.Entry(root,
			selectbackground = 'red',			# ��ѡ���ı��ı���ɫ����Ϊ��ɫ
			selectforeground = 'gray')			# ��ѡ���ı���ǰ��ɫ����Ϊ��ɫ
entry4.pack()
entry5 = Tkinter.Entry(root,
			state = Tkinter.DISABLED)			# ���ı�������Ϊ����
entry5.pack()
edit1 = Tkinter.Text(root,						# ���ɶ����ı������
			selectbackground = 'red',			# ��ѡ���ı��ı���ɫ����Ϊ��ɫ
			selectforeground = 'gray')			# ��ѡ���ı���ǰ��ɫ����Ϊ��ɫ
edit1.pack()
root.mainloop()								# ������Ϣѭ��
