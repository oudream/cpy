#  -*- coding: iso-8859-1 -*-
#  file: AutoRuns.py
#
# 导入所需要的模块
import string
from win32api import *
from win32con import *
# GetValues函数用于获得某注册表项下所有的项值
def GetValues(fullname):
    # 把完整的项拆分成根项和子项两部分
    name = string.split(fullname,'\\',1)
    # 打开相应的项，为了让该函数更通用
    # 使用了多个判断语句
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
        print 'err,no key named %s' (name[0])  
    # 查询项的项值数目     
    info = RegQueryInfoKey(key)
    # 遍历项值获得项值数据
    for i in range(0,info[1]):
       ValueName = RegEnumValue(key, i)
       # 调整项值名称长度，使输出更好看
       print string.ljust(ValueName[0],20),ValueName[1]
    # 关闭打开的项
    RegCloseKey(key)
# 因为GetValues函数比较通用，可以在其它脚本中调用
# 这里先检查脚本是否被其它脚本调用       
if __name__ == '__main__': 
    # 因为要要检查的项较多，故将将其放在列表中，便于增减  
    KeyNames = ['HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',\
                'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce',\
                'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx',\
                'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run',\
                'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce']
    # 遍历列表，调用GetValues函数，输出项值
    for KeyName in KeyNames:
        print KeyName
        GetValues(KeyName) 
