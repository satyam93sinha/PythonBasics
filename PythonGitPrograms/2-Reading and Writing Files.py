Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> with open('file1.txt', 'r')
SyntaxError: invalid syntax
>>> with open('file1.txt', 'r') as f:
	f.read()

	
'HEY'
>>> with open('file1.txt', 'w') as f:
	f.write('truncating HEY, writing HI')

	
26
>>> with open('file1.txt') as f:
	f.read()

	
'truncating HEY, writing HI'
>>> with open('file1.txt', 'x') as f:
	f.write('new file created, opened for writing mode')

	
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    with open('file1.txt', 'x') as f:
FileExistsError: [Errno 17] File exists: 'file1.txt'
>>> # the error itself clarifies, file of same name exists
>>> with open('file3.txt', 'x') as f:
	f.write('new file created, opened for writing mode')

	
41
>>> with open('file3.txt') as f:
	f.read()

	
'new file created, opened for writing mode'
>>> with open('file1.txt', 'a') as f:
	f.append('This time appending')

	
Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    f.append('This time appending')
AttributeError: '_io.TextIOWrapper' object has no attribute 'append'
>>> with open('file1.txt', 'a') as f:
	f.write('This time appending')

	
19
>>> with open('file1.txt') as f:
	f.read()

	
'truncating HEY, writing HIThis time appending'
>>> # the numbers as 19, 26 in output show that we successfully append
>>> # write into the files
>>> # the no. of letters written are shown in output.
>>> # now in file1.txt we have text as shown in read output above.
>>> # also, there's no append attribute, to append we use write() method.
>>> with open('file1.txt', 'b') as f:
	f.read()

	
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    with open('file1.txt', 'b') as f:
ValueError: Must have exactly one of create/read/write/append mode and at most one plus
>>> # 'b' mode is applicable only with any of the read/write/create/append
>>> # mode and a plus sign to add it to bytes mode.
>>> with open('file1.txt', 'r+b') as f:
	f.read()

	
b'truncating HEY, writing HIThis time appending'
>>> # generates the bytes version of text present in the file.
>>> # converts the string to bytes type.
>>> """It's a binary mode not bytes mode"""
"It's a binary mode not bytes mode"
>>> with open('file1.txt', 't') as f:
	f.read()

	
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    with open('file1.txt', 't') as f:
ValueError: Must have exactly one of create/read/write/append mode and at most one plus
>>> with open('file1.txt', 'w+t') as f:
	f.write('\n line change and writing in w+t mode')

	
37
>>> with open('file1.txt', 'r') as f:
	f.read()

	
'\n line change and writing in w+t mode'
>>> # overwritten existing file1.txt file, previous data truncated in file
>>> """By default files are opened, written in text mode
    which means even if we don't mention '+t' operations on file will
    continue to be in text mode"""
"By default files are opened, written in text mode\n    which means even if we don't mention '+t' operations on file will\n    continue to be in text mode"
>>> with open('file1.txt', '+') as f:
	f.read()
	f.write('new text, performing read and write simultaneously')

	
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    with open('file1.txt', '+') as f:
ValueError: Must have exactly one of create/read/write/append mode and at most one plus
>>> with open('file1.txt', 'r+w') as f:
	f.read()
	f.write('new text, performing read and write simultaneously')
	f.read()

	
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    with open('file1.txt', 'r+w') as f:
ValueError: must have exactly one of create/read/write/append mode
>>> with open('file1.txt', 'r+') as f:
	f.read()
	f.write('new text, performing read and write simultaneously')
	f.read()

	
'\n line change and writing in w+t mode'
50
''
>>> with open('file1.txt', 'r+') as f:
	f.read()
	f.write('new text, performing read and write simultaneously')
	print(f.read())

	
'\n line change and writing in w+t modenew text, performing read and write simultaneously'
50

>>> """While performing read and write simultaneously, the write()
    method appends text to the end of file rather overwritting it."""
'While performing read and write simultaneously, the write()\n    method appends text to the end of file rather overwritting it.'
>>> with open('file1.txt', 'U') as f:
	f.read()

	

Warning (from warnings module):
  File "__main__", line 1
DeprecationWarning: 'U' mode is deprecated
'\n line change and writing in w+t modenew text, performing read and write simultaneouslynew text, performing read and write simultaneously'
>>> # reads and returns the data present in file currently.
>>> with open('file1.txt', 'r+b', buffering=0) as f:
	f.read()

	
b'\r\n line change and writing in w+t modenew text, performing read and write simultaneouslynew text, performing read and write simultaneously'
>>> with open('file1.txt', 'w+b', buffering=0) as f:
	f.write()

	
Traceback (most recent call last):
  File "<pyshell#70>", line 2, in <module>
    f.write()
TypeError: write() takes exactly one argument (0 given)
>>> with open('file1.txt', 'w+b', buffering=0) as f:
	f.write('b')

	
Traceback (most recent call last):
  File "<pyshell#72>", line 2, in <module>
    f.write('b')
TypeError: a bytes-like object is required, not 'str'
>>> with open('file1.txt', 'w+b', buffering=0) as f:
	f.write(b('10'))

	
Traceback (most recent call last):
  File "<pyshell#74>", line 2, in <module>
    f.write(b('10'))
NameError: name 'b' is not defined
>>> b(10)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    b(10)
NameError: name 'b' is not defined
>>> type(b(10))
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    type(b(10))
NameError: name 'b' is not defined
>>> bytes(10)
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> type(bytes(10))
<class 'bytes'>
>>> bin(10)
'0b1010'
>>> type(bin(20))
<class 'str'>
>>> with open('file1.txt', 'w+b', buffering=0) as f:
	f.write(bytes(10))

	
10
>>> with open('file1.txt', 'r+b', buffering=0) as f:
	f.read()

	
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> with open('file1.txt', 'w+b', buffering=1) as f:
	f.write(bytes(10))

	
10
>>> with open('file1.txt', 'r+b', buffering=1) as f:
	f.read()

	
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> with open('file1.txt', 'r+t', buffering=0) as f:
	f.write('testing buffering')

	
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    with open('file1.txt', 'r+t', buffering=0) as f:
ValueError: can't have unbuffered text I/O
>>> # buffering=0 is only allowed in binary mode
>>> with open('file1.txt', 'r+t', buffering=1) as f:
	f.write('testing buffering')

	
17
>>> with open('file1.txt', buffering=1) as f:
	f.read()

	
'testing buffering'
>>> with open('file1.txt', 'r+b', encoding=ANSI) as f:
	f.read()

	
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    with open('file1.txt', 'r+b', encoding=ANSI) as f:
NameError: name 'ANSI' is not defined
>>> dir(encoding)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    dir(encoding)
NameError: name 'encoding' is not defined
>>> with open('file1.txt', 'r+b', encoding=ascii) as f:
	f.read()

	
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    with open('file1.txt', 'r+b', encoding=ascii) as f:
TypeError: open() argument 4 must be str or None, not builtin_function_or_method
>>> with open('file1.txt', 'r+b', encoding='ascii') as f:
	f.read()

	
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    with open('file1.txt', 'r+b', encoding='ascii') as f:
ValueError: binary mode doesn't take an encoding argument
>>> with open('file1.txt', 'r', encoding='ascii') as f:
	f.read()

	
'testing buffering'
>>> with open('file1.txt', 'r', encoding='cp863') as f:
	f.read()

	
'testing buffering'
>>> with open('file1.txt', 'r', encoding='cp864') as f:
	f.read()

	
'testing buffering'
>>> with open('file1.txt', 'r', encoding='big5') as f:
	f.read()

	
'testing buffering'
>>> with open('file1.txt', 'w', encoding='big5') as f;
SyntaxError: invalid syntax
>>> with open('file1.txt', 'w', encoding='big5') as f:
	f.write('traditional chinese encoding')

	
28
>>> with open('file1.txt', 'r', encoding='big5') as f:
	f.read()

	
'traditional chinese encoding'
>>> with open('file1.txt', 'r', encoding='ascii') as f:
	f.read()

	
'traditional chinese encoding'
>>> # encoding here shows no change.
>>> 
>>> with open('file1.txt', 'r', encoding='ascii', errors='strict') as f:
	f.read()

	
'traditional chinese encoding'
>>> locale.getpreferredencoding(False)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    locale.getpreferredencoding(False)
NameError: name 'locale' is not defined
>>> 'file1.txt'.getpreferredencoding(False)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    'file1.txt'.getpreferredencoding(False)
AttributeError: 'str' object has no attribute 'getpreferredencoding'
>>> with open('file1.txt', 'r', newline='\n') as f:
	f.read()

	
'traditional chinese encoding'
>>> with open('file1.txt', 'a', newline='\n') as f:
	f.write(' \n new line inserted')

	
20
>>> with open('file1.txt', 'r', newline='\n') as f:
	f.read()

	
'traditional chinese encoding \n new line inserted'
>>> with open('file1.txt', 'a', newline='\r\n') as f:
	f.write('new line inserted')

	
17
>>> with open('file1.txt', 'r', newline='\n') as f:
	f.read()

	
'traditional chinese encoding \n new line insertednew line inserted'
>>> with open('file1.txt', 'r') as f:
	f.read()

	
'traditional chinese encoding \n new line insertednew line inserted'
>>> with open('file1.txt', 'r') as f:
	f.read()

	
'traditional chinese encoding\nnew line inserted\nnew line inserted\nLines have been changed to check the output in python interpreter using read mode.'
>>> """When newline is None, by default, we have changed lines,
    inserted new lines in file and that can be seen from \n in the
    output we see above. Now, we'll check for what happens when
    newline=\n, \r\n is mentioned rather than it being None."""
"When newline is None, by default, we have changed lines,\n    inserted new lines in file and that can be seen from \n in the\n    output we see above. Now, we'll check for what happens when\n    newline=\n, \r\n is mentioned rather than it being None."
>>> with open('file1.txt', 'r', newline='\n') as f:
	f.read()

	
'traditional chinese encoding\r\nnew line inserted\r\nnew line inserted\r\nLines have been changed to check the output in python interpreter using read mode.'
>>> """\r is carriage return, returns the cursor position thereafter
    it finds new line so returns \n as was the case with newline=None.
    """
'\r is carriage return, returns the cursor position thereafter\n    it finds new line so returns \n as was the case with newline=None.\n    '
>>> with open('file1.txt', 'r', newline='') as f:
	f.read()

	
'traditional chinese encoding\r\nnew line inserted\r\nnew line inserted\r\nLines have been changed to check the output in python interpreter using read mode.'
>>> with open('file1.txt', 'r', newline='\r') as f:
	f.read()

	
'traditional chinese encoding\r\nnew line inserted\r\nnew line inserted\r\nLines have been changed to check the output in python interpreter using read mode.'
>>> 
