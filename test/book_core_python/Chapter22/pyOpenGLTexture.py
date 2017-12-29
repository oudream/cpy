# -*- coding:utf-8 -*-
# file: pyOpenGLTexture.py
#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import Image
class OpenGLWindow:
	def __init__(self, width = 640, height = 480, title = 'PyOpenGL'):	# ��ʼ��
		glutInit(sys.argv)						# ���������в���
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)	# ������ʾģʽ
		glutInitWindowSize(width, height)				# ���ô��ڴ�С
		self.window = glutCreateWindow(title)				# ��������
		glutDisplayFunc(self.Draw)					# ���ó������ƺ���
		glutIdleFunc(self.Draw)						# ���ÿ���ʱ�������ƺ���
		self.InitGL(width, height)					# ����OpenGL��ʼ������
		self.x = 0.2							# ��ת�Ƕ�����
		self.y = 0.2
		self.z = 0.2
	def Draw(self):								# ���Ƴ���
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)		# �����Ļ
		glLoadIdentity()						# ���ù۲����
		glTranslatef(0.0,0.0,-5.0)					# �ƶ�λ��
		glRotatef(self.x,1.0,0.0,0.0)					# ��X����ת
		glRotatef(self.y,0.0,1.0,0.0)					# ��Y����ת
		glRotatef(self.z,0.0,0.0,1.0)					# ��Z����ת
		glBegin(GL_QUADS)			    			# ����������
		glTexCoord2f(0.0, 0.0) 						# ��ǰ�������ͼ
		glVertex3f(-1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 0.0) 
		glVertex3f( 1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f( 1.0,  1.0,  1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f(-1.0,  1.0,  1.0)
		glTexCoord2f(1.0, 0.0) 						# �Ժ��������ͼ
		glVertex3f(-1.0, -1.0, -1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f(-1.0,  1.0, -1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f( 1.0,  1.0, -1.0)
		glTexCoord2f(0.0, 0.0)
		glVertex3f( 1.0, -1.0, -1.0)
		glTexCoord2f(0.0, 1.0) 						# �Զ��������ͼ 
		glVertex3f(-1.0,  1.0, -1.0)
		glTexCoord2f(0.0, 0.0) 
		glVertex3f(-1.0,  1.0,  1.0)
		glTexCoord2f(1.0, 0.0) 
		glVertex3f( 1.0,  1.0,  1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f( 1.0,  1.0, -1.0)
		glTexCoord2f(1.0, 1.0) 						# �Ե��������ͼ
		glVertex3f(-1.0, -1.0, -1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f( 1.0, -1.0, -1.0)
		glTexCoord2f(0.0, 0.0) 
		glVertex3f( 1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 0.0)
		glVertex3f(-1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 0.0) 						# ���Ҳ��������ͼ
		glVertex3f( 1.0, -1.0, -1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f( 1.0,  1.0, -1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f( 1.0,  1.0,  1.0)
		glTexCoord2f(0.0, 0.0) 
		glVertex3f( 1.0, -1.0,  1.0)
		glTexCoord2f(0.0, 0.0) 						# ������������ͼ
		glVertex3f(-1.0, -1.0, -1.0)
		glTexCoord2f(1.0, 0.0) 
		glVertex3f(-1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f(-1.0,  1.0,  1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f(-1.0,  1.0, -1.0)
		glEnd()			
		glutSwapBuffers()						# ��������
		self.x = self.x + 0.2						# ��ת�Ƕ�����
		self.y = self.y + 0.2
		self.z = self.z + 0.2
	def InitGL(self, width, height):					# OpenGL��ʼ������
    		self.LoadTextures()						# ��������
    		glEnable(GL_TEXTURE_2D)						# ��������ӳ��
		glClearColor(0.0, 0.0, 0.0, 0.0)				# ��Ϊ��ɫ���� 
		glClearDepth(1.0)						# ������Ȼ���
		glDepthFunc(GL_LESS)						# ������Ȳ�������
		glEnable(GL_DEPTH_TEST)						# ������Ȳ���
		glShadeModel(GL_SMOOTH)						# ����ƽ����Ӱ
		glMatrixMode(GL_PROJECTION)					# ���ù۲����
		glLoadIdentity()						# ���ù۲����
		gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)	# ������Ļ�߿��
		glMatrixMode(GL_MODELVIEW)					# ���ù۲����
	def LoadTextures(self):							# ��������ͼƬ
		image = Image.open('python.bmp')				# ��ͼƬ
		width = image.size[0]						# ͼ����
		height = image.size[1]						# ͼ��߶�
		image = image.tostring('raw', 'RGBX', 0, -1)			# ת��ͼ��
		glBindTexture(GL_TEXTURE_2D, glGenTextures(1))   		# ��������
		glPixelStorei(GL_UNPACK_ALIGNMENT,1)
		glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 
				0, GL_RGBA, GL_UNSIGNED_BYTE, image)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
	def MainLoop(self):							# ������Ϣѭ��
		glutMainLoop()
window = OpenGLWindow()								# ��������
window.MainLoop()								# ������Ϣѭ��
