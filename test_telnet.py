Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from telnetlib import Telnet
>>> ttt = Telnet('10.88.126.56, port = 3100, 10)
	     
SyntaxError: EOL while scanning string literal
>>> print(ttt)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(ttt)
NameError: name 'ttt' is not defined
>>> ttt = Telnet('10.88.126.56, port = 3100)
	     
SyntaxError: EOL while scanning string literal
>>> with Telnet('10.88.126.56, port = 3100) as tn:
	    
SyntaxError: EOL while scanning string literal
>>> ttt = Telnet('10.88.126.56', port = 3100, 10)
SyntaxError: positional argument follows keyword argument
>>> with Telnet('10.88.126.56', port = 3100) as tn:
tn.interact()
SyntaxError: expected an indented block
>>> with Telnet('10.88.126.56', port = 3100) as tn:
    tn.interact()
    ttt = tn.read_all()
print (ttt)
SyntaxError: invalid syntax
>>> with Telnet('10.88.126.56', port = 3100) as tn:
    tn.read_until('50PA-540 Connection Open')
    tn.write(b'RA1\n')
    ttt=tn.read_all()
print(ttt)
SyntaxError: invalid syntax
>>> 
= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 2, in <module>
    with Telnet('10.88.126.56', port = 3100) as tn:
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
TimeoutError: [WinError 10060] Попытка установить соединение была безуспешной, т.к. от другого компьютера за требуемое время не получен нужный отклик, или было разорвано уже установленное соединение из-за неверного отклика уже подключенного компьютера
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 2, in <module>
    with Telnet('10.88.128.56', port = 3100) as tn:
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 2, in <module>
    with Telnet('10.88.128.56', port = 3100, timeout = 10) as tn:
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 2, in <module>
    with Telnet('10.88.128.54', port = 3100, timeout = 10) as tn:
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 2, in <module>
    with Telnet('10.88.128.56', port = 3100, timeout = 10) as tn:
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 2, in <module>
    with Telnet('10.88.128.56', port = 3100, timeout = 10) as tn:
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================

>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 2, in <module>
    with Telnet('10.88.128.56', port = 3100, timeout = 5) as tn:
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 2, in <module>
    with Telnet('10.88.128.56', 3100, timeout = 5) as tn:
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 2, in <module>
    with Telnet('10.88.128.56', 3100) as tn:
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 3, in <module>
    Telnet.open('10.88.128.56', port = 3100, timeout = 5)
TypeError: open() missing 1 required positional argument: 'host'
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 3, in <module>
    Telnet.open('10.88.128.56', port = 3100, timeout = 5)
TypeError: open() missing 1 required positional argument: 'host'
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 3, in <module>
    Telnet.open(host = '10.88.128.56', port = 3100, timeout = 5)
TypeError: open() missing 1 required positional argument: 'self'
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 4, in <module>
    Telnet.open(host, port = 3100, timeout = 5)
TypeError: open() missing 1 required positional argument: 'host'
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 4, in <module>
    Telnet.open(HOST, port = 3100, timeout = 5)
TypeError: open() missing 1 required positional argument: 'host'
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 5, in <module>
    Telnet.open(HOST, port = 3100, timeout = 5)
TypeError: open() missing 1 required positional argument: 'host'
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 8, in <module>
    tn = Telnet(HOST, port = 3100, timeout = 5)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 


>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 8, in <module>
    tn = Telnet(HOST, port = 3100, timeout = 5)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 8, in <module>
    tn = Telnet(HOST, 3100, 5)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 8, in <module>
    tn = Telnet(HOST, 3100, 5)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
RA1
>>> 
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
b'RA1'
>>> 
KeyboardInterrupt
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 8, in <module>
    tn = Telnet(HOST, '3100',1)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
socket.timeout: timed out
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 8, in <module>
    tn = Telnet(HOST, 3100,1)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
socket.timeout: timed out
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 8, in <module>
    tn = Telnet(HOST, 3100)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 8, in <module>
    tn = Telnet(HOST, 3100)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 15, in <module>
    promt = "%s>"%(host)
NameError: name 'host' is not defined
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 19, in <module>
    tn = telnetlib.Telnet(HOST, 3100, timeout=5)
NameError: name 'telnetlib' is not defined
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 19, in <module>
    tn = Telnet(HOST, 3100, timeout=5)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Traceback (most recent call last):
  File "C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py", line 37, in <module>
    tn = telnetlib.Telnet(HOST, 3100)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 218, in __init__
    self.open(host, port, timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\telnetlib.py", line 235, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 808, in create_connection
    raise err
  File "C:\Users\пк\AppData\Local\Programs\Python\Python38-32\lib\socket.py", line 796, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================

Atten #1 = 62dB

>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================

Atten #1 = 62dB

Atten #1 = 63dB

>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================

Atten #1 = 63dB




>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================

Atten #1 = 61dB




>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================

Atten #1 = 61dB


Atten #1 = 63dB


>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================

Atten #1 = 61dB


Atten #1 = 60dB


>>> 
================= RESTART: C:/Users/пк/AppData/Local/Programs/Python/Python38-32/test_telnet.py ================
Было:  
Atten #1 = 63dB

Стааим 60:  
Стало:  Atten #1 = 60dB

Ставим 63:  
Стало2:  Atten #1 = 63dB

>>> 