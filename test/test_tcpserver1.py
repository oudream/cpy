import socket

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # s = socket.socket()
s.bind(address)
s.listen(5)

ss, addr = s.accept()
print('got connected from', addr)

msg='欢迎访问菜鸟教程！'+ "\r\n"
ss.send(msg.encode('utf-8'))
ra = ss.recv(512)
print(ra)

ss.close()
s.close()