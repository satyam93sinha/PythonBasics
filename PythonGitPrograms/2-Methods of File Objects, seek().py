Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> with open('file3.txt') as f:
	f.seek()

	
Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    f.seek()
TypeError: seek() takes at least 1 argument (0 given)
>>> with open('file3.txt') as f:
	f.seek(-4, 2)

	
Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    f.seek(-4, 2)
io.UnsupportedOperation: can't do nonzero end-relative seeks
>>> with open('file3.txt') as f:
	f.tell()
	f.seek(-4, 2)

	
0
Traceback (most recent call last):
  File "<pyshell#7>", line 3, in <module>
    f.seek(-4, 2)
io.UnsupportedOperation: can't do nonzero end-relative seeks

>>> with open('file3.txt') as f:
	f.read(10)
	f.tell()
	f.seek(-4, 1)

	
'new file c'
10
Traceback (most recent call last):
  File "<pyshell#9>", line 4, in <module>
    f.seek(-4, 1)
io.UnsupportedOperation: can't do nonzero cur-relative seeks
>>> with open('file3.txt') as f:
	f.read(10)
	f.tell()
	f.seek(2, 1)
	f.read()

	
'new file c'
10
Traceback (most recent call last):
  File "<pyshell#12>", line 4, in <module>
    f.seek(2, 1)
io.UnsupportedOperation: can't do nonzero cur-relative seeks
>>> f = open('file2.txt')
>>> f.read()
'Hi, file2appending append'
>>> f.encoding()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    f.encoding()
TypeError: 'str' object is not callable
>>> f.mode
'r'
>>> f.encoding
'cp1252'
>>> f.buffer
<_io.BufferedReader name='file2.txt'>
>>> f.fileno
<built-in method fileno of _io.TextIOWrapper object at 0x03E01B30>
>>> f.errors
'strict'
>>> f.seekable
<built-in method seekable of _io.TextIOWrapper object at 0x03E01B30>
>>> f.seekable()
True
>>> f.seek(4)
4
>>> f.read()
'file2appending append'
>>> f.seek(-3, 2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    f.seek(-3, 2)
io.UnsupportedOperation: can't do nonzero end-relative seeks
>>> f.seek(0, 2)
25
>>> f.close()
>>> f.closed
True
>>> f = open('file2.txt', 'r+b')
>>> f.seek(-4, 2)
21
>>> f.read()
b'pend'
>>> # returns the last 4 characters from the end.
>>> # setting target to -4 and whence to 2, counts and displays last 4 chars
>>> # from end
>>> 
