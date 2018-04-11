#  -*- coding: iso-8859-1 -*-
#  file: AutoRuns.py
#
# ��������Ҫ��ģ��
import string
from win32api import *
from win32con import *
# GetValues�������ڻ��ĳע����������е���ֵ
def GetValues(fullname):
    # �����������ֳɸ��������������
    name = string.split(fullname,'\\',1)
    # ����Ӧ���Ϊ���øú�����ͨ��
    # ʹ���˶���ж����
    if name[0] == 'HKEY_LOCAL_MACHINE':
        key = RegOpenKey(HKEY_LOCAL_MACHINE,name[1], 0, KEY_READ)
    elif name[0] == 'HKEY_CURRENT_USER':
        key = RegOpenKey(HKEY_CURRENT_USER,name[1], 0, KEY_READ)
    elif name[0] == 'HKEY_CLASSES_ROOT':
        key = RegOpenKey(HKEY_CLASSES_ROOT,name[1], 0, KEY_READ)
    elif name[0] == 'HKEY_CURRENT_CONFIG':
        key = RegOpenKey(HKEY_CURRENT_CONFIG,name[1], 0, KEY_READ)
    elif name[0] == 'HKEY_USERS':
        key = RegOpenKey(HKEY_USERS,name[1], 0, KEY_READ)
    else:
        print(('err,no key named %s' (name[0])))  
    # ��ѯ�����ֵ��Ŀ     
    info = RegQueryInfoKey(key)
    # ������ֵ�����ֵ����
    for i in range(0,info[1]):
       ValueName = RegEnumValue(key, i)
       # ������ֵ���Ƴ��ȣ�ʹ������ÿ�
       print((string.ljust(ValueName[0],20),ValueName[1]))
    # �رմ򿪵���
    RegCloseKey(key)
# ��ΪGetValues�����Ƚ�ͨ�ã������������ű��е���
# �����ȼ��ű��Ƿ������ű�����       
if __name__ == '__main__': 
    # ��ΪҪҪ������϶࣬�ʽ���������б��У���������  
    KeyNames = ['HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',\
                'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce',\
                'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx',\
                'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run',\
                'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce']
    # �����б�����GetValues�����������ֵ
    for KeyName in KeyNames:
        print(KeyName)
        GetValues(KeyName) 
