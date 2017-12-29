# -*- coding:utf-8 -*-
# file: TkinterCanvas.py
#
import Tkinter								# ����Tkinterģ��
root = Tkinter.Tk()
canvas = Tkinter.Canvas(root,
			width = 600,					# ָ��Canvas����Ŀ��
			height = 480,					# ָ��Canvas����ĸ߶�
			bg = 'white')					# ָ��Canvas����ı���ɫ
im = Tkinter.PhotoImage(file='python.gif')				# ʹ��PhotoImage��ͼƬ
canvas.create_image(300,50,image = im)					# ʹ��create_image��ͼƬ��ӵ�Canvas�����
canvas.create_text(302,77,						# ʹ��create_text���������꣨302��77������������
		text = 'Use Canvas'					# ���������ֵ�����
		,fill = 'gray')						# ���������ֵ���ɫΪ��ɫ
canvas.create_text(300,75,
		text = 'Use Canvas',
		fill = 'blue')
canvas.create_polygon(290,114,316,114,330,130,				# ʹ��create_polygon��������������
		      310,146,284,146,270,130)
canvas.create_oval(280,120,320,140,					# ʹ��create_oval����������Բ
		fill = 'white')						# ������Բ�ð�ɫ���
canvas.create_line(250,130,350,130)					# ʹ��create_line����һ���ӣ�250,130������350,130����ֱ��
canvas.create_line(300,100,300,160)
canvas.create_rectangle(90,190,510,410,					# ʹ��create_rectangle����һ������
		width=5)						# ���þ����߿�Ϊ5������
canvas.create_arc(100, 200, 500, 400, 					# ʹ��create_arc����Բ��
		start=0, extent=240, 					# ����Բ������ֹ�Ƕ�
		fill="pink")						# ����Բ�������ɫ
canvas.create_arc(103,203,500,400, 
		start=241, extent=118, 
		fill="red")
canvas.pack()								# ��Canvas��ӵ�������
root.mainloop()

