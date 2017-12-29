# -*- coding:utf-8 -*-
# file: pyOpenGLDraw2D.py
#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math
class OpenGLWindow:
	def __init__(self, width = 640, height = 480, title = 'PyOpenGL'):	# ��ʼ��
		glutInit(sys.argv)						# ���������в���
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)	# ������ʾģʽ
		glutInitWindowSize(width, height)				# ���ô��ڴ�С
		self.window = glutCreateWindow(title)				# ��������
		glutDisplayFunc(self.Draw)					# ���ó������ƺ���
		self.InitGL(width, height)					# ����OpenGL��ʼ������
	def Draw(self):								# ���Ƴ���
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()						# ���ù۲����
		glTranslatef(-2.0, 2.0, -6.0)					# �ƶ�λ��
		glBegin(GL_LINES)						# ����ֱ��
		glVertex3f(0.0, 0.0, 0.0)					# ֱ�ߵ�һ������
		glVertex3f(2.0, 0.0, 0.0)					# ֱ�ߵڶ�������
		glEnd()								# ��������
		glTranslatef(3.0, 0.0, 0.0)					# �ƶ�λ��
		glBegin(GL_POLYGON)						# ͨ�����ƶ������ģ��Բ
		i = 0
		while( i <= 3.14 *2 ):
			x = 0.5 * math.cos(i)
			y = 0.5 * math.sin(i)
			glVertex3f(x, y, 0.0)
			i = i + 0.01
		glEnd()
		glTranslatef(-2, -3.0, 0.0)					# �ƶ�λ��
		glBegin(GL_POLYGON)                 				# ����������
		glVertex3f(0.0, 1.0, 0.0)
		glVertex3f(1.0, -1.0, 0.0)
		glVertex3f(-1.0, -1.0, 0.0)
		glEnd()
		glTranslatef(2.5, 0.0, 0.0)					# �ƶ�λ��
		glBegin(GL_QUADS)                   				# �����ı���
		glVertex3f(-1.0, 1.0, 0.0)
		glVertex3f(1.0, 1.0, 0.0)
		glVertex3f(1.0, -1.0, 0.0)
		glVertex3f(-1.0, -1.0, 0.0)
		glEnd()
		glutSwapBuffers()						# ��������
	def InitGL(self, width, height):					# OpenGL��ʼ������
		glClearColor(0.0, 0.0, 0.0, 0.0)				# ��Ϊ��ɫ���� 
		glClearDepth(1.0)						# ������Ȼ���
		glDepthFunc(GL_LESS)						# ������Ȳ�������
		glEnable(GL_DEPTH_TEST)						# ������Ȳ���
		glShadeModel(GL_SMOOTH)						# ����ƽ����Ӱ
		glMatrixMode(GL_PROJECTION)					# ���ù۲����
		glLoadIdentity()						# ���ù۲����
		gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)	# ������Ļ�߿��
		glMatrixMode(GL_MODELVIEW)					# ���ù۲����
	def MainLoop(self):							# ������Ϣѭ��
		glutMainLoop()
window = OpenGLWindow()								# ��������
window.MainLoop()								# ������Ϣѭ��
