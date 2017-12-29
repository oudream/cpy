# -*- coding:utf-8 -*-
# file: pyOpenGLWindow.py
#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
class OpenGLWindow:
	def __init__(self, width = 640, height = 480, title = 'PyOpenGL'):	# ��ʼ��
		glutInit(sys.argv)						# ���������в���
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)	# ������ʾģʽ
		glutInitWindowSize(width, height)				# ���ô��ڴ�С
		self.window = glutCreateWindow(title)				# ��������
		glutDisplayFunc(self.Draw)					# ���ó������ƺ���
		self.InitGL(width, height)					# ����OpenGL��ʼ������
	def Draw(self):								# ���Ƴ���
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)		# �����Ļ����Ȼ���
		glLoadIdentity()						# ���ù۲����
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
