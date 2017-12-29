# -*- coding:utf-8 -*-
# file: gtalk.py
#
import xmpp									# ����ģ��
def GetMessage(client, message):						# ��Ϣ������
	text = message.getBody()						# �����Ϣ����
	people = message.getFrom()						# ��÷�����
	print 'GET: %s FROM: %s' % (text, people)				# ��ӡ��Ϣ
	client.send(xmpp.protocol.Message(people,				# ������Ϣ
		'GET: ' + text,typ="chat"))
user = raw_input('User:')							# ��ȡ�û���
password = raw_input('Password:')						# ��ȡ����
jid = xmpp.protocol.JID(user + '@gmail.com')					# ����JID
client = xmpp.Client(jid.getDomain(),debug=[])					# �����ͻ���
client.connect(('talk.google.com',5222))					# ���ӷ�����
client.auth(user, password)							# �û���֤
Roster = client.getRoster()							# ��ȡ�û��б�
names = Roster.getItems()							# ��ȡ�û���
for name in names:								# ѭ������û�
    status = Roster.getStatus(name)
    print name,
    print status
client.RegisterHandler('message',GetMessage)					# ע����Ϣ�ص�����
client.sendInitPresence()							# ��������
while 1:									# ����ѭ��
	try:
		client.Process(1)
	except KeyboardInterrupt:						# ����Ctrl+c
		break
