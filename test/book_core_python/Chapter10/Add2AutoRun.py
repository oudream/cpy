#  -*- coding: iso-8859-1 -*-
#  file: Add2AutoRun.py
#
import win32api
import win32con
# Ҫ��ӵ���ֵ����
name = 'SetIE'
# Ҫ��ӵ�Python�ű���·��
path = 'C:\\SetIE.py'
# ע�������
KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
# �쳣����
try:
    # ��ע�����
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,\
                              KeyName,\
                              0,\
                              win32con.KEY_ALL_ACCESS)
    # ������ֵ
    win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
    # �ر�ע���
    win32api.RegCloseKey(key)
except:
    print 'error'
print 'added that!'
