Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> with open('file1.txt', 'r') as f:
	f.read(size=0)

	
Traceback (most recent call last):
  File "<pyshell#3>", line 2, in <module>
    f.read(size=0)
TypeError: read() takes no keyword arguments
>>> with open('file1.txt', 'r') as f:
	f.read(size=1)

	
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    f.read(size=1)
TypeError: read() takes no keyword arguments
>>> with open('file1.txt', 'r') as f:
	f.read(1)

	
't'
>>> # reads some quantity of data and returns it.
>>> with open('file1.txt', 'r') as f:
	f.read(10)

	
'traditiona'
>>> with open('file1.txt', 'r') as f:
	f.readline()

	
'traditional chinese encoding\n'
>>> # reads a line at a time, includes new line if found else no \n.
>>> # reads single line from the file. This is correct, technically.
>>> with open('file1.txt', 'r') as f:
	f.readlines()

	
['traditional chinese encoding\n', 'new line inserted\n', 'new line inserted\n', 'Lines have been changed to check the output in python interpreter using read mode.']
>>> # last line doesn't have \n character bcoz we didn't insert new line in end
>>> # ... in file.
>>> # readlines() reads all the lines of a file, a line at a time.
>>> with open('file1.txt', 'r') as f:
	for line in f:
		print(line)

		
traditional chinese encoding

new line inserted

new line inserted

Lines have been changed to check the output in python interpreter using read mode.
>>> # read exactly as it was written in file and then displayed.
>>> """For reading lines from a ﬁle, you can loop over the ﬁle object.
    This is memory eﬃcient, fast, and leads to simple code."""
'For reading lines from a ﬁle, you can loop over the ﬁle object.\n    This is memory eﬃcient, fast, and leads to simple code.'
>>> with open('file1.txt', 'r') as f:
	list(f)

	
['traditional chinese encoding\n', 'new line inserted\n', 'new line inserted\n', 'Lines have been changed to check the output in python interpreter using read mode.']
>>> # returns all lines of file in list
>>> with open('file1.txt', 'r') as f:
	tuple(f)

	
('traditional chinese encoding\n', 'new line inserted\n', 'new line inserted\n', 'Lines have been changed to check the output in python interpreter using read mode.')
>>> # returns all lines of file as tuple.
>>> with open('file1.txt', 'a') as f:
	val=('appending', 'tuple')
	f.write(val)

	
Traceback (most recent call last):
  File "<pyshell#36>", line 3, in <module>
    f.write(val)
TypeError: write() argument must be str, not tuple
>>> with open('file1.txt', 'a') as f:
	val=('appending', 'tuple')
	f.write(str(val))

	
22
>>> with open('file1.txt', 'r') as f:
	f.read()

	
"traditional chinese encoding\nnew line inserted\nnew line inserted\nLines have been changed to check the output in python interpreter using read mode.('appending', 'tuple')"
>>> with open('file1.txt', 'r') as f:
	f.read()
	f.tell()

	
"traditional chinese encoding\nnew line inserted\nnew line inserted\nLines have been changed to check the output in python interpreter using read mode.('appending', 'tuple')"
172
>>> with open('file3.txt', 'r') as f:
	f.read()
	f.tell()

	
'new file created, opened for writing mode'
41
>>> # returns an integer giving the ﬁle object’s current position in the ﬁle
>>> with open('file3.txt', 'r') as f:
	f.read()
	f.seek(whence=5)

	
'new file created, opened for writing mode'
Traceback (most recent call last):
  File "<pyshell#48>", line 3, in <module>
    f.seek(whence=5)
TypeError: seek() takes no keyword arguments
>>> with open('file3.txt', 'r') as f:
	f.read()
	f.seek(5)

	
'new file created, opened for writing mode'
5
>>> with open('file3.txt', 'r') as f:
	f.read()
	f.seek(5)
	f.read()

	
'new file created, opened for writing mode'
5
'ile created, opened for writing mode'
>>> with open('file3.txt', 'r') as f:
	f.read()
	f.seek(5, 30)
	f.read()
	f.tell()

	
'new file created, opened for writing mode'
Traceback (most recent call last):
  File "<pyshell#56>", line 3, in <module>
    f.seek(5, 30)
ValueError: invalid whence (30, should be 0, 1 or 2)
>>> with open('file3.txt', 'r') as f:
	f.read()
	f.seek(5)
	f.read()
	f.tell()

	
'new file created, opened for writing mode'
5
'ile created, opened for writing mode'
41
>>> # f.tell() reads from start of file to its end
>>> # f.seek(5) changes cursor position, starts from 6th byte now, check output
>>> with open('file3.txt', 'r') as f:
	f.read()
	f.seek(5, 1)
	f.read()
	f.tell()

	
'new file created, opened for writing mode'
Traceback (most recent call last):
  File "<pyshell#62>", line 3, in <module>
    f.seek(5, 1)
io.UnsupportedOperation: can't do nonzero cur-relative seeks
>>> with open('file3.txt', 'r') as f:
	f.read()
	f.seek(5, 1)
	f.read()
	f.tell()

	
'new file created, opened for writing mode'
Traceback (most recent call last):
  File "<pyshell#64>", line 3, in <module>
    f.seek(5, 1)
io.UnsupportedOperation: can't do nonzero cur-relative seeks
>>> # refer to 26-Methods of file objects.txt, 1 for current position
>>> with open('file3.txt', 'r') as f:
	f.read()
	f.seek(-5, 1)
	f.read()
	f.tell()

	
'new file created, opened for writing mode'
Traceback (most recent call last):
  File "<pyshell#67>", line 3, in <module>
    f.seek(-5, 1)
io.UnsupportedOperation: can't do nonzero cur-relative seeks
>>> with open('file3.txt', 'r') as f:
	f.read()
	f.seek(-5, 2)
	f.read()
	f.tell()

	
'new file created, opened for writing mode'
Traceback (most recent call last):
  File "<pyshell#69>", line 3, in <module>
    f.seek(-5, 2)
io.UnsupportedOperation: can't do nonzero end-relative seeks
>>> with open('file3.txt', 'r') as f:
	f.read()
	f.seek(-5, 2)

	
'new file created, opened for writing mode'
Traceback (most recent call last):
  File "<pyshell#71>", line 3, in <module>
    f.seek(-5, 2)
io.UnsupportedOperation: can't do nonzero end-relative seeks
>>> dir(seek)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    dir(seek)
NameError: name 'seek' is not defined
>>> help(seek)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    help(seek)
NameError: name 'seek' is not defined
>>> with open('file3.txt', 'r') as f:
	f.read()
	f.seek(-5, 2)

	
'new file created, opened for writing mode'
Traceback (most recent call last):
  File "<pyshell#75>", line 3, in <module>
    f.seek(-5, 2)
io.UnsupportedOperation: can't do nonzero end-relative seeks
>>> 
