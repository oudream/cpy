# -*- coding:utf-8 -*-
# file: TkinterCheck.py
#
import Tkinter							# ����Tkinterģ��
root = Tkinter.Tk()
r = Tkinter.StringVar()						# ʹ��StringVar�����ַ����������ڵ�ѡ�����
r.set('1')							# ��ʼ������ֵ
radio = Tkinter.Radiobutton(root,				# ���ɵ�ѡ�����
			variable = r, 				# ���õ�ѡ������ı���
			value = '1',				# ����ѡ�е�ѡ��ʱ���������ı�����ֵ����r��ֵ
			text = 'Radio1')			# ���õ�ѡ����ʾ���ı�
radio.pack()
radio = Tkinter.Radiobutton(root,
			variable = r,
			value = '2',				# ��ѡ�иõ�ѡ��ʱr��ֵΪ2
			text = 'Radio2' )
radio.pack()
radio = Tkinter.Radiobutton(root,
			variable = r,
			value = '3',				# ��ѡ�иõ�ѡ��ʱr��ֵΪ3
			text = 'Radio3' )
radio.pack()
radio = Tkinter.Radiobutton(root,
			variable = r,
			value = '4',				# ��ѡ�иõ�ѡ��ʱr��ֵΪ4
			text = 'Radio4' )
radio.pack()
c = Tkinter.IntVar()						# ʹ��IntVar�������ͱ������ڸ�ѡ��
c.set(1)
check = Tkinter.Checkbutton(root,
			text = 'Checkbutton',			# ���ø�ѡ����ı�
			variable = c,				# ���ø�ѡ������ı���
			onvalue = 1,				# ��ѡ�и�ѡ��ʱ��c��ֵΪ1
			offvalue = 2)				# ��δѡ�и�ѡ��ʱ��c��ֵΪ2
check.pack()
root.mainloop()
print r.get()							# ���r��ֵ
print c.get()							# ���c��ֵ
