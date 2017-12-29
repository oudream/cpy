#  -*- coding:utf-8 -*-
#  file: ModifyMemory.py
#
from ctypes import *
# ����_PROCESS_INFORMATION�ṹ��
class _PROCESS_INFORMATION(Structure):
	_fields_ = [('hProcess', c_void_p),
		    ('hThread', c_void_p),
		    ('dwProcessId', c_ulong),
		    ('dwThreadId', c_ulong)]
# ����_STARTUPINFO�ṹ��
class _STARTUPINFO(Structure):
	_fields_ = [('cb',c_ulong),
  		    ('lpReserved', c_char_p),  
  		    ('lpDesktop', c_char_p),  
  		    ('lpTitle', c_char_p), 
  		    ('dwX', c_ulong),
  		    ('dwY', c_ulong), 
  		    ('dwXSize', c_ulong),
  		    ('dwYSize', c_ulong), 
  		    ('dwXCountChars', c_ulong),
  		    ('dwYCountChars', c_ulong), 
  		    ('dwFillAttribute', c_ulong), 
  		    ('dwFlags', c_ulong),
  		    ('wShowWindow', c_ushort),  
  		    ('cbReserved2', c_ushort), 
  		    ('lpReserved2', c_char_p),  
  		    ('hStdInput', c_ulong),  
  		    ('hStdOutput', c_ulong),
  		    ('hStdError', c_ulong)]
# ����NORMAL_PRIORITY_CLASS
NORMAL_PRIORITY_CLASS = 0x00000020
# ����kernel32.dll
kernel32 = windll.LoadLibrary("kernel32.dll")
# ���CreateProcess������ַ
CreateProcess = kernel32.CreateProcessA
# ���ReadProcessMemory������ַ
ReadProcessMemory = kernel32.ReadProcessMemory
# ���WriteProcessMemory������ַ
WriteProcessMemory = kernel32.WriteProcessMemory
TerminateProcess = kernel32.TerminateProcess
# �����ṹ��
ProcessInfo = _PROCESS_INFORMATION()
StartupInfo = _STARTUPINFO()
# Ҫ�����޸ĵ��ļ�
file = 'ModifyMe.exe'
# Ҫ�޸ĵ��ڴ��ַ
address = 0x0040103c
# ��������ַ
buffer = c_char_p("_") 
# ������ֽ���
bytesRead = c_ulong(0)
# ��������С
bufferSize =  len(buffer.value)
# ��������
if CreateProcess(file, 0, 0, 0, 0, NORMAL_PRIORITY_CLASS, 0, 0, byref(StartupInfo), byref(ProcessInfo)):
	# ��ȡҪ�޸ĵ��ڴ��ַ�����ж��Ƿ���Ҫ�޸ĵ��ļ�
	if ReadProcessMemory(ProcessInfo.hProcess, address, buffer, bufferSize, byref(bytesRead)):
		if buffer.value == '\x74':
			# �޸Ļ�������ֵ������д���ڴ�
			buffer.value = '\x75'
			# �޸��ڴ�
			if WriteProcessMemory(ProcessInfo.hProcess, address, buffer, bufferSize, byref(bytesRead)):
				print '�ɹ���д�ڴ�!'
			else:
				print 'д�ڴ����!'
		else:
			print '���˴�����ļ�!'
			# �������Ҫ�޸ĵ��ļ�������ֹ����
			TerminateProcess(ProcessInfo.hProcess,0)
	else:
		print '���ڴ����!'
else:
	print '���ܴ�������!'
