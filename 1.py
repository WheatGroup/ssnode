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

# /9b5df634-201e-11e7-847c-620c9e705744
x = tran('add: {"server_port":8010, "password":"outsideworldABCD"}')
print x
print tback(x)


x = tran('remove: {"server_port",8001}')
print x
print tback(x)


x = tran('remove: {"server_port":8001}')
print x
print tback(x)

x = tran('ping')
print x
print tback(x)
