# -*- coding:utf-8 -*-
# file: rename.py
#
import os
perfix = 'Python'						# perfix Ϊ����������ļ���ʼ�ַ�
length = 2 							# length Ϊ��ȥperfix���ļ���Ҫ�ﵽ�ĳ���
base = 1								# �ļ�������ʼ��
format = 'mdb'							# �ļ��ĺ�׺��
# ����PadLeft���ļ�����ȫ��ָ������
# str ΪҪ��ȫ���ַ�
# num ΪҪ�ﵽ�ĳ���
# padstr δ�ﵽ��������ӵ��ַ�
def PadLeft(str , num , padstr):
	stringlength = len (str)
	n = num - stringlength
	if n >=0 :
		str=padstr * n + str
	return str
# Ϊ�˱������������������ʾ�û�
print 'the files in %s will be renamed' % os.getcwd()
input = raw_input('press y to continue\n')		# ��ȡ�û�����
if input != 'y':							# �ж��û����룬�Ծ����Ƿ�ִ������������
	exit()
filenames = os.listdir(os.curdir)				# ��õ�ǰĿ¼�е�����
# �ӻ�����1��Ϊ�����±� i = i + 1�ڵ�һ��ִ��ʱ���ڻ���
i = base - 1
for filename in filenames:					# ����Ŀ¼�����ݣ���������������
	i = i+1
	# �жϵ�ǰ·���Ƿ�Ϊ�ļ������Ҳ��ǡ�rename.py��
	if filename != "rename.py" and os.path.isfile(filename):
		name = str(i)					# ��iת�����ַ�
		name = PadLeft(name,length,'0')	# ��name��ȫ��ָ������
		t = filename.split('.')				# �ָ��ļ������Լ�����Ƿ�����Ҫ�޸ĵ�����
		m = len(t)
		if format == '':					# ���δָ���ļ����ͣ�����ĵ�ǰĿ¼�������ļ�
			os.rename(filename,perfix+name+'.'+t[m-1])
		else:							# ����ֻ�޸�ָ������
			if t[m-1] == format:
				os.rename(filename,perfix+name+'.'+t[m-1])
			else:
				i = i - 1				# ��֤i����
	else:
		i = i - 1						# ��֤i����

