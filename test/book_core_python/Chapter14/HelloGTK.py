# -*- coding:utf-8 -*-
# file: HelloGTK.py
#
import pygtk					# ����pygtkģ��
pygtk.require('2.0')				# ����pygtk�����gtk�汾
import gtk					# ����gtkģ��
window = gtk.Window()				# �������ڶ���
window.set_title('PyGTK')			# ���ô��ڱ���
window.set_default_size(300, 200)		# ���ô��ڴ�С
window.show()					# ��ʾ����
gtk.main()					# ������Ϣѭ��
