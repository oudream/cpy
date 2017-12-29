# -*- coding:utf-8 -*-
# file: pyOpenGLDraw3D.py
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
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)		# �����Ļ
		glLoadIdentity()						# ���ù۲����
		glTranslatef(1.5,0.0,-7.0)					# �ƶ�λ��
		glRotatef(45,1.0,1.0,1.0)					# �ֱ���X��Y��Z����ת45��
		glBegin(GL_QUADS)						# ��ʼ����������
		glColor3f(1.0,0.0,0.0)						# ������ɫΪ��ɫ
		glVertex3f( 1.0, 1.0,-1.0)					# ����������Ķ���
		glVertex3f(-1.0, 1.0,-1.0)
		glVertex3f(-1.0, 1.0, 1.0)
		glVertex3f( 1.0, 1.0, 1.0)
		glColor3f(0.0,1.0,0.0)						# ������ɫΪ��ɫ
		glVertex3f( 1.0,-1.0, 1.0)
		glVertex3f(-1.0,-1.0, 1.0)
		glVertex3f(-1.0,-1.0,-1.0)
		glVertex3f( 1.0,-1.0,-1.0)
		glColor3f(0.0,0.0,1.0)						# ������ɫΪ��ɫ
		glVertex3f( 1.0, 1.0, 1.0)
		glVertex3f(-1.0, 1.0, 1.0)
		glVertex3f(-1.0,-1.0, 1.0)
		glVertex3f( 1.0,-1.0, 1.0)
		glColor3f(1.0,0.0,0.0)
		glVertex3f( 1.0,-1.0,-1.0)
		glVertex3f(-1.0,-1.0,-1.0)
		glVertex3f(-1.0, 1.0,-1.0)
		glVertex3f( 1.0, 1.0,-1.0)
		glColor3f(0.0,1.0,0.0)
		glVertex3f(-1.0, 1.0, 1.0)
		glVertex3f(-1.0, 1.0,-1.0)
		glVertex3f(-1.0,-1.0,-1.0)
		glVertex3f(-1.0,-1.0, 1.0)
		glColor3f(0.0,0.0,1.0)
		glVertex3f( 1.0, 1.0,-1.0)
		glVertex3f( 1.0, 1.0, 1.0)
		glVertex3f( 1.0,-1.0, 1.0)
		glVertex3f( 1.0,-1.0,-1.0)
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
