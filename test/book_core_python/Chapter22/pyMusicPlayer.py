# -*- coding:utf-8 -*-
# file: pyMusicPlayer.py
#
import Tkinter										# ����Tkinterģ��
import tkFileDialog									# ����tkFileDialogģ��
from win32com.client import Dispatch
class Window:
	def __init__(self):
		self.root = root = Tkinter.Tk()						# ��������
		buttonAdd = Tkinter.Button(root, text = 'Add',
				command = self.add)
		buttonAdd.place(x = 150, y = 15)
		buttonPlay = Tkinter.Button(root, text = 'Play',
				command = self.play)
		buttonPlay.place(x = 200, y = 15)
		buttonPause = Tkinter.Button(root, text = 'Pause',
				command = self.pause)
		buttonPause.place(x= 250, y = 15)
		buttonStop = Tkinter.Button(root, text = 'Stop',
				command = self.stop)
		buttonStop.place(x= 300, y = 15)
		buttonNext = Tkinter.Button(root, text = 'Next',
				command = self.next)
		buttonNext.place(x = 350, y = 15)
		frame = Tkinter.Frame(root, bd=2)
		self.playList = Tkinter.Text(frame)
		scrollbar = Tkinter.Scrollbar(frame)
		scrollbar.config(command=self.playList.yview)
		self.playList.pack(side = Tkinter.LEFT)
		scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
		frame.place(y = 50)
		self.wmp = Dispatch('WMPlayer.OCX')					# ��WMPlayer.OCX
	def MainLoop(self):								# ������Ϣѭ��
		self.root.minsize(510,380)
		self.root.maxsize(510,380)
		self.root.mainloop()
	def add(self):									# ��Ӳ����ļ�
		file = tkFileDialog.askopenfilename(title = 'Python Music Player',
			filetypes=[('MP3', '*.mp3'), 
				('WMA', '*.wma'), ('WAV', '*.wav')])
		if file:
			media = self.wmp.newMedia(file)
			self.wmp.currentPlaylist.appendItem(media)
			self.playList.insert(Tkinter.END, file + '\n')
	def play(self):
		self.wmp.controls.play()						# �����ļ�
	def pause(self):
		self.wmp.controls.pause()						# ��ͣ
	def next(self):
		self.wmp.controls.next()						# ��һ��
	def stop(self):
		self.wmp.controls.stop()						# ֹͣ
window = Window()
window.MainLoop()
