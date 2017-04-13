import threading
import time
import socket
import uuid

from flask import Flask
from flask import request
from flask import abort

cli = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
cli.bind('/tmp/client890700891211111' + str(uuid.uuid1()) + '.sock')  # address of the client
cli.connect('/var/run/shadowsocks-manager.sock')  # address of Shadowsocks manager

#cli.send(b'ping')
#print(cli.recv(1506))  # You'll receive 'pong'

#cli.send(b'add: {"server_port":8001, "password":"7cd308cc059"}')
#print(cli.recv(1506))  # You'll receive 'ok'

#cli.send(b'remove: {"server_port":8001}')
#print(cli.recv(1506))  # You'll receive 'ok'


abc_q = []
abc_s = threading.Semaphore()
abc_result = ''

class SummingThread(threading.Thread):
	def __init__(self):
		super(SummingThread, self).__init__()

	def run(self):
		global abc_s
		global abc_q
		global abc_result
		abc_s.acquire()
		print abc_q
		cli.send(abc_q[0])
		abc_q = []
		abc_result = cli.recv(1506)
		print abc_result
		abc_s.release()

def tranchar(x):
	a = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_ {}\":,"
	i = a.find(x)
	return a[(len(a) + i+5)%len(a)]

def tranback(x):
	a = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_ {}\":,"
	i = a.find(x)
	return a[(len(a) + i -5)%len(a)]

def tran(data):
        re = ""
        for i in xrange(len(data)):
                re += tranchar(data[i]);
        return re;
def tback(data):
        re = ""
        for i in xrange(len(data)):
                re += tranback(data[i]);
        return re;

app = Flask(__name__)

@app.route("/9b5df634-201e-11e7-847c-620c9e705744")
def reslove():
	global abc_result
	data = tback(request.args.get('oo'));
	print data
	if data.startswith('ping') or data.startswith('add: ') or data.startswith('remove: '):
		abc_s.acquire()
		abc_q.append(data);
		abc_s.release()
		a = SummingThread()
		a.start();
		a.join();
		return abc_result
	else:
		abort(403)
print __name__
print 'running'

if __name__ == '__main__':
	app.run()
