# -*- coding:utf-8 -*-
# file: pyftp.py
#
import string
from ftplib import FTP								# ��ftplibģ���е���FTP
bufsize = 1024									# ���û�������С
def Get(filename):								# �����ļ�
	command = 'RETR ' + filename
	ftp.retrbinary(command, open(filename,'wb').write, bufsize)
	print '���سɹ�'
def Put(filename):								# �ϴ��ļ�
	command = 'STOR ' + filename
	filehandler = open(filename,'rb')
	ftp.storbinary(command,filehandler,bufsize)
	filehandler.close()
	print '�ϴ��ɹ�'
def PWD():									# ��ȡ��ǰĿ¼
	print ftp.pwd()
def Size(filename):								# ��ȡ�ļ���С
	print ftp.size(filename)
def Help():									# �������
	print '''
	==================================
		Simple Python FTP 
	==================================
	cd		�����ļ���
	delete		ɾ���ļ�
	dir		��ȡ��ǰ�ļ��б�
	get		�����ļ�
	help		����
	mkdir		�����ļ���
	put		�ϴ��ļ�
	pwd		��ȡ��ǰĿ¼
	rename		�������ļ�
	rmdir		ɾ���ļ���
	size		��ȡ�ļ���С
	'''
server = raw_input('������FTP��������ַ:')					# ��ȡ��������ַ
ftp = FTP(server)								# ���ӵ���������ַ
username = raw_input('�������û���:')						# ��ȡ�û���
password = raw_input('����������:')						# ��ȡ�ֵ�
ftp.login(username,password)              					# ��¼FTP
print ftp.getwelcome()								# ��ȡ��ӭ��Ϣ
actions  = {'dir':ftp.dir, 'pwd': PWD, 'cd':ftp.cwd, 'get':Get,			# �������Ӧ�ĺ����ֵ�
		'put':Put, 'help':Help, 'rmdir': ftp.rmd, 
		'mkdir': ftp.mkd, 'delete':ftp.delete,
		'size':Size, 'rename':ftp.rename}
while True:									# ����ѭ��
	print 'pyftp>',								# �����ʾ��
	cmds = raw_input()							# ��ȡ����
	cmd = string.split(cmds)						# �����밴�ո�ָ�
	try:									# �쳣����
		if len(cmd) == 1:						# �ж������Ƿ��в���
			if string.lower(cmd[0]) == 'quit':			# �������Ϊquit���˳�ѭ��
				break
			else:
				actions[string.lower(cmd[0])]()			# �����������Ӧ�ĺ���
		elif len(cmd) == 2:						# ����������һ�����������
			actions[string.lower(cmd[0])](cmd[1])			# �����������Ӧ�ĺ���
		elif len(cmd) == 3:						# �����������������������
			actions[string.lower(cmd[0])](cmd[1],cmd[2])		# �����������Ӧ�ĺ���
		else:
			print '�������'
	except:
		print '�������'
ftp.quit()									# �˿�����
