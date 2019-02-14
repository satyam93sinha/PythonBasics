Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Queues
>>> import collections.dequeue
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import collections.dequeue
ModuleNotFoundError: No module named 'collections.dequeue'
>>> import collections.deque
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import collections.deque
ModuleNotFoundError: No module named 'collections.deque'
>>> import collections.deque
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import collections.deque
ModuleNotFoundError: No module named 'collections.deque'
>>> # there isn't any module named specifically as collections.deque
>>> from collections import deque
>>> # we just import deque from collections, will learn about it in detail
>>> # in MODULES section or after it.
>>> clear
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> 

>>> 
>>> from collections import deque
>>> queue = deque(['erry', 'weird', 'awkward'])
>>> queue.append(['eerie','uncanny'])
>>> queue.popleft()
'erry'
>>> queue
deque(['weird', 'awkward', ['eerie', 'uncanny']])
>>> queue.pop()
['eerie', 'uncanny']
>>> # this immediate queue.pop() functioned as STACK, LIFO.
>>> queue.append('eerie')
>>> queue
deque(['weird', 'awkward', 'eerie'])
>>> queue.popleft()
'weird'
>>> queue
deque(['awkward', 'eerie'])
>>> #Queue works fine, FIFO, we use popleft() to delete and return the
>>> #first entered element.
>>> queues = ['eerie', 'weird']
>>> queues.append('Unnatural')
>>> queues.popleft()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    queues.popleft()
AttributeError: 'list' object has no attribute 'popleft'
>>> #The AttributeError is returned because 'list' doesn't have popleft() as
>>> # attribute, it can only be seen in deque which is imported through
>>> # collections.
>>> 
