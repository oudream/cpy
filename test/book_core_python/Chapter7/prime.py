# -*- coding:utf-8 -*-
# file: prime.py
#
import math
# isprime�����ж�һ�������Ƿ�Ϊ������
# ���i�ܱ�2��i��ƽ�����ڵ�����һ����������
# ��i��������������0������i������������1��
def isprime(i):
	for t in range( 2, int(math.sqrt(i)) + 1 ):
		if i % t == 0:			
			return 0	
		else:
			return 1
print '100~110֮��������У�'
for i in range(100,110):
	if isprime(i):
		print i
