# -*- coding:utf-8 -*-
# file : GetFunction.py
# 
import re
import sys
def DealWithFunc(s):
	r = re.compile(r'''
		(?<=def\s)	# ǰ�߱��뺬��def��def���һ���ո�
		\w+		# ƥ�亯����
		\(.*?\)		# ƥ�����
		(?=:)		# ��߱����һ����:��
		''',re.X)	# ���ñ���ѡ�����ģʽ�е�ע��
	return r.findall(s)
def DealWithVar(s):
	vars = []		# ����һ���б���Ϊ����������������
	r = re.compile(r'''
		\b		# ƥ�䵥�ʿ�ʼ
		\w+		# ƥ�������
		(?=\s=)		# ����ΪΪ������ֵ�����
		''',re.X)
	vars.extend(r.findall(s))
	r = re.compile(r'''
		(?<=for\s)	# �������λ��for����е����
		\w+		# ƥ�������
		\s		# ƥ��ո�
		(?=in)		# ƥ��in
		''',re.X)	# ���ñ���ѡ�����ģʽ�е�ע��
	vars.extend(r.findall(s))
	return vars
# �ж��������Ƿ������룬û����Ҫ������Ҫ������ļ�
if len(sys.argv) == 1:
	sour = raw_input('������Ҫ������ļ�·��')
else:
	sour = sys.argv[1]
file = open(sour)		# ���ļ�
s = file.readlines()		# ���ļ��������ж����s��
file.close()			# �ر��ļ�
print '********************************'
print sour,'�еĺ����У�'
print '********************************'
i = 0				# iΪ�������ڵ��к�
# ѭ������ÿһ�У�ƥ�����еĺ���������������ڵ��кţ��Լ�������ԭ��
for line in s:
	i = i + 1
	function = DealWithFunc(line)
	if len(function) == 1:
		print 'Line: ',i,'\t',function[0]
print '********************************'
print sour,'�еı����У�'
print '********************************'
i = 0				# �˴�iΪ�������ڵ��к�
# ѭ������ÿһ�У�ƥ�����еı���������������ڵ��кţ��Լ�������
for line in s:
	i = i + 1
	var = DealWithVar(line)
	if len(var) == 1:
		print 'Line: ',i,'\t',var[0]
