#  -*- coding: iso-8859-1 -*-
#  file: SetIE.py
#
import datetime
import string
import win32api
import win32con
# Ҫ�޸ĵ�ע�����
keyname = 'Software\Microsoft\Internet Explorer\Main'
# Ҫ����Ϊ��ҳ����ַ
page = 'www.python.org'
# ��ȡ��ǰ����
today = datetime.date.today()
# �����ڸ�ʽ��Ϊxxxx��xx��xx�յ���ʽ
title = today.strftime('%Y')+'��'+today.strftime('%m')+'��'+today.strftime('%d')+'��'
# �쳣����
try:
    # ��ע������þ��
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, keyname, 0, win32con.KEY_ALL_ACCESS)
    # ��ȡ"Start Page"����ֵ����
    StartPage = win32api.RegQueryValueEx(key, 'Start Page')
except:
    print 'error'
else:
    # �ж���ҳ�Ƿ�ΪҪ�޸ĵ���ҳ������������޸�
    if StartPage[0] != page:
        win32api.RegSetValueEx(key, 'Start Page', 0, win32con.REG_SZ, page)
    # ����IE�ı�����Ϊxxxx��xx��xx��
    win32api.RegSetValueEx(key, 'Window Title', 0, win32con.REG_SZ, title)
    # �ر�ע���
    win32api.RegCloseKey(key)    