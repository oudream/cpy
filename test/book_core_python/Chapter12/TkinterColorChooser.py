# -*- coding:utf-8 -*-
# file: TkinterColorChooser.py
#
import Tkinter										# ����Tkinterģ��
import tkColorChooser									# ����tkColorChooserģ��
def ChooseColor():									# ��ť�¼�������
	r = tkColorChooser.askcolor(title = 'Python Tkinter')				# ������ɫѡ��Ի���
	print r										# �������ֵ
root = Tkinter.Tk()
button = Tkinter.Button(root,text = 'Choose Color',					# ������ť
		command = ChooseColor)							# ָ����ť�¼�������
button.pack()
root.mainloop()										# ������Ϣѭ��
