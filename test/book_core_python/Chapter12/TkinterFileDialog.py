# -*- coding:utf-8 -*-
# file: TkinterFileDialog.py
#
import Tkinter										# ����Tkinterģ��
import tkFileDialog									# ����tkFileDialogģ��
def FileOpen():										# ��ť�¼�������
	r = tkFileDialog.askopenfilename(title = 'Python Tkinter',			# �������ļ��Ի���
			filetypes=[('Python', '*.py *.pyw'),('All files', '*')]	)	# ָ���ļ�����ΪPython�ű�
	print r										# �������ֵ
def FileSave():										# ��ť�¼�������
	r = tkFileDialog.asksaveasfilename(title = 'Python Tkinter',			# ���������ļ��Ի���
			initialdir=r'E:\Python\code',					# ָ����ʼ��Ŀ¼
			initialfile = 'test.py')					# ָ����ʼ���ļ�
	print r
root = Tkinter.Tk()
button1 = Tkinter.Button(root,text = 'File Open',					# ������ť
		command = FileOpen)							# ָ����ť�¼�������
button1.pack(side='left')
button2 = Tkinter.Button(root,text = 'File Save',
		command = FileSave)							# ָ����ť�¼�������
button2.pack(side='left')
root.mainloop()										# ������Ϣѭ��

