# -*- coding:utf-8 -*-
# file: TkinterButton.py
#
import Tkinter							# ����Tkinterģ��
root = Tkinter.Tk()
button1 = Tkinter.Button(root, 			
			anchor = Tkinter.E,			# ָ���ı����뷽ʽ
			text = 'Button1',			# ָ����ť�ϵ��ı�
			width = 40,				# ָ����ť�Ŀ�ȣ��൱��40���ַ�
			height = 5)				# ָ����ť�ĸ߶ȣ��൱��5���ַ�
button1.pack()							# ����ť��ӵ�����
button2 = Tkinter.Button(root, 			
			text = 'Button2',	
			bg = 'blue')				# ָ����ť�ı���ɫ
button2.pack()
button3 = Tkinter.Button(root, 			
			text = 'Button3',	
			width = 14,				# ָ����ť�Ŀ��
			height = 1)				# ָ����ť�ĸ߶�
button3.pack()
button4 = Tkinter.Button(root, 			
			text = 'Button4',	
			width = 60,		
			height = 5,		
			state = Tkinter.DISABLED)		# ָ����ťΪ����״̬
button4.pack()
root.mainloop()							# ������Ϣѭ��
