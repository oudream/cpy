# -*- coding:utf-8 -*-
# file: pyDirectSound.py
#
import pywintypes									# ����ģ��
import struct
from win32com.directsound import directsound
import Tkinter
import tkFileDialog
WAV_HEADER_SIZE = struct.calcsize('<4sl4s4slhhllhh4sl')					# ����WAVͷ
class Window:
	def __init__(self):
		self.root = root = Tkinter.Tk()						# �������
		buttonAdd = Tkinter.Button(root, text = 'Add',
				command = self.add)
		buttonAdd.pack(side = 'left')
		buttonPlay = Tkinter.Button(root, text = 'Play',
				command = self.play)
		buttonPlay.pack(side = 'left')
		buttonStop = Tkinter.Button(root, text = 'Stop',
				command = self.stop)
		buttonStop.pack(side = 'left')
	def MainLoop(self):								# ������Ϣѭ��
		self.root.mainloop()
	def add(self):									# ��Ӳ����ļ�
		self.file = tkFileDialog.askopenfilename(
				title = 'Python DirectSound',
				filetypes=[('WAV', '*.wav')])
	def play(self):									# �����ļ�
		f = open(self.file, 'rb')						# ���ļ�
		header = f.read(WAV_HEADER_SIZE)					# ��ȡWAV�ļ�ͷ
		(riff, riffsize, wave, fmt, fmtsize, 
			format, nchannels, samplespersecond,
			datarate, blockalign, bitspersample, 
			data, size) =\
	 	struct.unpack('<4sl4s4slhhllhh4sl', header)				# ��ȡ����ֵ
	    	if riff != 'RIFF' or fmtsize != 16 or fmt != 'fmt ' or data != 'data':	# �ж��ļ���ʽ
			raise 'Data Error'
		wfx = pywintypes.WAVEFORMATEX()						# ����WAVEFORMATEX�ṹ
		wfx.wFormatTag = format
		wfx.nChannels = nchannels
		wfx.nSamplesPerSec = samplespersecond
		wfx.nAvgBytesPerSec = datarate
		wfx.nBlockAlign = blockalign
		wfx.wBitsPerSample = bitspersample
		d = directsound.DirectSoundCreate(None, None)				# ʹ��DirectSound��������
		d.SetCooperativeLevel(None, directsound.DSSCL_PRIORITY)
		sdesc = directsound.DSBUFFERDESC()
		sdesc.dwFlags = (
				directsound.DSBCAPS_STICKYFOCUS | 
				directsound.DSBCAPS_CTRLPOSITIONNOTIFY
				)
		sdesc.dwBufferBytes = size
		sdesc.lpwfxFormat = wfx
		self.buffer = buffer = d.CreateSoundBuffer(sdesc, None)
		buffer.Update(0, f.read(size))
		buffer.Play(0)
	def stop(self):
		self.buffer.Stop()							# ֹͣ
window = Window()
window.MainLoop()
