Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Users\\Sinha\\AppData\\Local\\Programs\\Python\\Python37-32'
>>> os.chdir("F://")
>>> os.getcwd()
'F:\\'
>>> dir(os.getcwd())
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> os.getcwd().__doc__
"str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."
>>> print(os.getcwd().__doc__)
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
>>> os.path.join(os.getcwd(), os.system("mkdir today"))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    os.path.join(os.getcwd(), os.system("mkdir today"))
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\ntpath.py", line 115, in join
    genericpath._check_arg_types('join', path, *paths)
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\genericpath.py", line 149, in _check_arg_types
    (funcname, s.__class__.__name__)) from None
TypeError: join() argument must be str or bytes, not 'int'
>>> os.system("mkdir today")
1
>>> os.system("mkdir tomorrow")
0
>>> dir(os.system())
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dir(os.system())
TypeError: system() missing required argument 'command' (pos 1)
>>> dir(os.system)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
>>> print(os.system.__doc__)
Execute the command in a subshell.
>>> # folders named today and tomorrow are created but why does it return
>>> # 1 in the first, 0 in second is the question.
>>> os.system("del tomorrow")
0
>>> #  deletes directory tomorrow, opens subshell for permission in y/n
>>> os.system("delete tomorrow")
1
>>> # didn't delete it.
>>> os.system("del tomorrow")
0
>>> os.getcwd()
'F:\\'
>>> os.system("del tomorrow")
1
>>> os.system("del tom")
0
>>> os.system("dir")
0
>>> os.system("del starpattern.class")
0
>>> os.path.join(os.getcwd(), "/today")
'F:/today'
>>> os.getcwd()
'F:\\'
>>> os.chdir(os.path.join(os.getcwd(), "/today"))
>>> os.getcwd()
'F:\\today'
>>> # use it wisely, permanently deletes file
>>> import shutil
>>> dir(shutil)
['Error', 'ExecError', 'ReadError', 'RegistryError', 'SameFileError', 'SpecialFileError', '_ARCHIVE_FORMATS', '_BZ2_SUPPORTED', '_LZMA_SUPPORTED', '_UNPACK_FORMATS', '_ZLIB_SUPPORTED', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_basename', '_check_unpack_options', '_copyxattr', '_destinsrc', '_ensure_directory', '_find_unpack_format', '_get_gid', '_get_uid', '_make_tarball', '_make_zipfile', '_ntuple_diskusage', '_rmtree_safe_fd', '_rmtree_unsafe', '_samefile', '_unpack_tarfile', '_unpack_zipfile', '_use_fd_functions', 'chown', 'collections', 'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree', 'disk_usage', 'errno', 'fnmatch', 'get_archive_formats', 'get_terminal_size', 'get_unpack_formats', 'getgrnam', 'getpwnam', 'ignore_patterns', 'make_archive', 'move', 'nt', 'os', 'register_archive_format', 'register_unpack_format', 'rmtree', 'stat', 'sys', 'unpack_archive', 'unregister_archive_format', 'unregister_unpack_format', 'which']
>>> print(shutil.__doc__)
Utility functions for copying and archiving files and directory trees.

XXX The functions here don't copy the resource fork or other metadata on Mac.


>>> shutil.disk_usage.__doc__
"Return disk usage statistics about the given path.\n\n        Returned values is a named tuple with attributes 'total', 'used' and\n        'free', which are the amount of total, used and free space, in bytes.\n        "
>>> shutil.disk_usage
<function disk_usage at 0x03D41AE0>
>>> shutil.disk_usage()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    shutil.disk_usage()
TypeError: disk_usage() missing 1 required positional argument: 'path'
>>> shutil.disk_usage(os.getcwd())
usage(total=96635711488, used=27662004224, free=68973707264)
>>> # returns usage in bytes
>>> os.getcwd()
'F:\\today'
>>> shutil.copyfile("newText.txt", "secondText.txt")
'secondText.txt'
>>> with open("secondText.txt")
SyntaxError: invalid syntax
>>> 
>>> 
>>> with open("secondText.txt", 'r') as f:
	f.readlines()

	
['first new text\n', 'testing shutil.copy in python, module shutil']
>>> # proves copying of file.
>>> os.chdir("F://")
>>> shutil.copyfile("today", "tomorrow")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    shutil.copyfile("today", "tomorrow")
  File "C:\Users\Sinha\AppData\Local\Programs\Python\Python37-32\lib\shutil.py", line 120, in copyfile
    with open(src, 'rb') as fsrc:
PermissionError: [Errno 13] Permission denied: 'today'
>>> # this module, copyfile attribute can only be used to copy files, no folders
>>> import glob
>>> glob.glob("F://today", "*.txt")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    glob.glob("F://today", "*.txt")
TypeError: glob() takes 1 positional argument but 2 were given
>>> os.chdir("F://today")
>>> os.getcwd()
'F:\\today'
>>> glob.glob("*.txt")
['newText.txt', 'secondText.txt']
>>> # returns the file names with the mentioned extensions in list.
>>> print(glob.__doc__)
Filename globbing utility.
>>> dir(glob)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_glob0', '_glob1', '_glob2', '_iglob', '_ishidden', '_isrecursive', '_iterdir', '_rlistdir', 'escape', 'fnmatch', 'glob', 'glob0', 'glob1', 'has_magic', 'iglob', 'magic_check', 'magic_check_bytes', 'os', 're']
>>> glob.__package__
''
>>> glob.magic_check.__doc__
'Compiled regular expression object.'
>>> glob.has_magic.__doc__
>>> dir(glob.has_magic)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> print(glob.has_magic.__doc__)
None
>>> glob.iglob.__doc__
"Return an iterator which yields the paths matching a pathname pattern.\n\n    The pattern may contain simple shell-style wildcards a la\n    fnmatch. However, unlike fnmatch, filenames starting with a\n    dot are special cases that are not matched by '*' and '?'\n    patterns.\n\n    If recursive is true, the pattern '**' will match any files and\n    zero or more directories and subdirectories.\n    "
>>> print(glob.iglob.__doc__)
Return an iterator which yields the paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    
>>> os.getcwd()
'F:\\today'
>>> n = glob.iglob("**")
>>> next(n)
'newText.txt'
>>> for i in n:
	print(i)

	
secondText.txt
>>> # Thus, iglob is a generator returning patterned filenames
>>> n = glob.iglob(".py")
>>> try:
	for i in n:
		print(i)
except Exception as e:
	print(e)

	
>>> def check():
	try:
		for i in n:
			print(i)
	except Exception as e:
		print(e)

		
>>> check()
>>> 
>>> n = glob.iglob(".py")
>>> next(n)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    next(n)
StopIteration
>>> def check():
	try:
		for i in n:
			print(i)
	except StopIteration:
		print("StopIteration")

		
>>> check()
>>> n = glob.iglob(".py")
>>> check()
>>> for i in n:
	print(i)

	
>>> # stop iteration isn't raised by for loop, for simply breaks encountering it
>>> import sys
>>> print(sys.argv)
['']
>>> print(sys.argv.__doc__)
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
>>> print(sys.argv([1,2,3]))
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    print(sys.argv([1,2,3]))
TypeError: 'list' object is not callable
>>> import re
>>> re.fullmatch(r'\aab[a-z]*', 'aab go to jaab without traab')
>>> re.findall(r'\aab[a-z]*', 'aab go to jaab without traab')
[]
>>> re.findall(r'\baab[a-z]*', 'aab go to jaab without traab')
['aab']
>>> re.fullmatch(r'\baab[a-z]*', 'aab go to jaab without traab')
>>> re.fullmatch(r'\baab[a-z]*', 'aab')
<re.Match object; span=(0, 3), match='aab'>
>>> 
