# -*- coding:utf-8 -*-
# file: TkinterPopupmenu.py
#
import Tkinter 
root = Tkinter.Tk()
menu = Tkinter.Menu(root, tearoff=0)				# �����˵�
menu.add_command(label="Copy")					# �򵯳�ʽ�˵������Copy����
menu.add_command(label="Paste")					# �򵯳�ʽ�˵������Paste����
menu.add_separator()						# �򵯳�ʽ�˵�����ӷָ���
menu.add_command(label="Cut")					# �򵯳�ʽ�˵������Cut����
def popupmenu(event):						# �����Ҽ��¼�������
    menu.post(event.x_root, event.y_root)			# ��ʾ�˵�
root.bind("<Button-3>", popupmenu)				# ���������а��Ҽ��¼�
root.mainloop()
