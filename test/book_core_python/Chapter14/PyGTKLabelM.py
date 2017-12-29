# -*- coding:utf-8 -*-
# file: PyGTKLabelM.py
#
import pygtk											# ����pygtkģ��
pygtk.require('2.0')										# ����pygtk�����gtk�汾
import gtk											# ����gtkģ��
class MyWindow():										# ���崰����
	def __init__(self, title, width, height):						# �����ʼ������
		self.window = gtk.Window()							# ���ɴ��ڶ���
		self.window.set_title(title)							# ���ô��ڱ���
		self.window.set_default_size(width, height)					# ���ô��ڴ�С
		vbox = gtk.VBox(False, 5)							# ��������Box����
       		hbox1 = gtk.HBox(False, 5)							# ����ˮƽBox����
		hbox2 = gtk.HBox(False, 5)
		label1 = gtk.Label('Label1')							# ������ǩ
		label1.set_angle(90)								# ���ñ�ǩ�Ƕ�
		label2 = gtk.Label('Label2')
		label2.set_angle(270)
		label3 = gtk.Label('Label3')
		label4 = gtk.Label('Label4')
		label5 = gtk.Label('Label5')
		hbox1.pack_start(label1)							# ��Box��������ӱ�ǩ
		hbox1.pack_start(label2)
		hbox2.pack_start(label3)
		hbox2.pack_end(label4)
		hbox2.pack_end(label5)
		vbox.pack_start(hbox1)								# ��Box�������������Box����
		vbox.pack_start(hbox2)
		self.window.add(vbox)								# �򴰿����Box����
		label1.show()									# ��ʾ��ǩ
		label2.show()
		label3.show()
		label4.show()
		label5.show()
		hbox1.show()									# ��ʾBox����
		hbox2.show()
		vbox.show()
		self.window.show()								# ��ʾ����
	def main(self):										# ����main����
		gtk.main()									# ����gtk.main����
window = MyWindow('PyGTK', 300, 200)								# �������ڶ���
window.main()

