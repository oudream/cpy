#  -*- coding: iso-8859-1 -*-
#  file: Add2AutoRun.py
#
import win32api
import win32con
# 要添加的项值名称
name = 'SetIE'
# 要添加的Python脚本的路径
path = 'C:\\SetIE.py'
# 注册表项名
KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
# 异常处理
try:
    # 打开注册表项
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,\
                              KeyName,\
                              0,\
                              win32con.KEY_ALL_ACCESS)
    # 设置项值
    win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
    # 关闭注册表
    win32api.RegCloseKey(key)
except:
    print('error')
print('added that!')
