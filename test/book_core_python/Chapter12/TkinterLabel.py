# -*- coding:utf-8 -*-
# file: TkinterLabel.py
#
import Tkinter								# ����Tkinterģ��
root = Tkinter.Tk()
label1 = Tkinter.Label(root,
			anchor = Tkinter.E,				# �����ı���λ��
			bg = 'blue',					# ���ñ�ǩ����ɫ
			fg = 'red',					# ���ñ�ǩǰ��ɫ
			text = 'Python',				# ���ñ�ǩ�е��ı�
			width = 30,					# ���ñ�ǩ�Ŀ��Ϊ30
			height = 5)					# ���ñ�ǩ�ĵĸ߶�Ϊ5
label1.pack()
label2 = Tkinter.Label(root,
			text = 'Python GUI\nTkinter',			# ���ñ�ǩ�е��ı������ַ�����ʹ�û��з�
			justify = Tkinter.LEFT,				# ���ö����ı�Ϊ�����
			width = 30,
			height = 5)
label2.pack()
label3 = Tkinter.Label(root,
			text = 'Python GUI\nTkinter',
			justify = Tkinter.RIGHT,			# ���ö����ı�Ϊ�Ҷ���
			width = 30,
			height = 5)
label3.pack()
label4 = Tkinter.Label(root,
			text = 'Python GUI\nTkinter',
			justify = Tkinter.CENTER,			# ���ö����ı�Ϊ���ж���
			width = 30,
			height = 5)
label4.pack()
root.mainloop()
