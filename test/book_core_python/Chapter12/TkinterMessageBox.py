# -*- coding:utf-8 -*-
# file: TkinterMessageBox.py
#
import Tkinter										# ����Tkinterģ��
import tkMessageBox									# ����tkMessageBoxģ��
def cmd():										# ��ť��Ϣ������
	global n									# ʹ��ȫ�ֱ���n
	global buttontext								# ʹ��ȫ�ֱ���buttontext
	n = n + 1
	if n == 1:									# �ж�n��ֵ����ʾ��ͬ����Ϣ��
		tkMessageBox.askokcancel('Python Tkinter','askokcancel')		# ʹ��askokcancel����
		buttontext.set('skquestion')						# ���İ�ť�ϵ�����
	elif n == 2:
		tkMessageBox.askquestion('Python Tkinter','skquestion')			# ʹ��askquestion����
		buttontext.set('askyesno')
	elif n == 3:
		tkMessageBox.askyesno('Python Tkinter','askyesno')			# ʹ��askyesno����
		buttontext.set('showerror')
	elif n == 4:
		tkMessageBox.showerror('Python Tkinter','showerror')			# ʹ��showerror����
		buttontext.set('showinfo')
	elif n == 5:
		tkMessageBox.showinfo('Python Tkinter','showinfo')			# ʹ��showinfo����
		buttontext.set('showwarning')
	else :
		n = 0									# ��n��ֵΪ0���¿�ʼѭ��
		tkMessageBox.showwarning('Python Tkinter','showwarning')		# ʹ��showwarning����
		buttontext.set('askokcancel')
n = 0											# Ϊn����ʼֵ
root = Tkinter.Tk()
buttontext = Tkinter.StringVar()							# ���ɹ�����ť���ֵı���
buttontext.set('askokcancel')								# ����buttontextֵ
button = Tkinter.Button(root,								# ���ɰ�ť
		textvariable = buttontext,						# ���ù�������
		command = cmd)								# �����¼�������
button.pack()
root.mainloop()										# ������Ϣѭ��
