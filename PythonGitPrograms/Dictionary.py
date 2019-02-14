Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict_def = {}
>>> dict_def
{}
>>> type(dict_def)
<class 'dict'>
>>> dict_def = {,}
SyntaxError: invalid syntax
>>> dict_def = {:}
SyntaxError: invalid syntax
>>> dict_def = {"":""}
>>> dict_def
{'': ''}
>>> #dict_def is a dictionary with empty key and value pair.
>>> dict_def_1 = {key=value
		  
SyntaxError: invalid syntax
>>> dict_def_1 = {key=value}
		  
SyntaxError: invalid syntax
dict_def_1 = {key=value}
>>> dict_def_1 = {'key'='value'}
		  
SyntaxError: invalid syntax
>>> dict_def_1 = {'key':'value'}
		  
>>> dict_def_1
		  
{'key': 'value'}
>>> dict_def_1.keys()
		  
dict_keys(['key'])
>>> #From above we understand that '=' can't be taken as syntax for dict
		  
>>> #definition for defining key:value pair, only ':' can be.
		  
>>> #also, key and value aren't any defined variable.
		  
>>> 
		  
>>> dict_def_2 = {('key1','value1'),('key2','value2')}
		  
>>> dict_def_2
		  
{('key2', 'value2'), ('key1', 'value1')}
>>> type(dict_def_2)
		  
<class 'set'>
>>> dict_def_2.keys('key1')
		  
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    dict_def_2.keys('key1')
AttributeError: 'set' object has no attribute 'keys'
>>> dict_def_1.keys('key1')
		  
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dict_def_1.keys('key1')
TypeError: keys() takes no arguments (1 given)
>>> dict_def_2 = ([('key1','value1'),('key2','value2')])
		  
>>> dict_def_2
		  
[('key1', 'value1'), ('key2', 'value2')]
>>> type(dict_def_2)
		  
<class 'list'>
>>> dict_def_2 = dict([('key1','value1'),('key2','value2')])
		  
>>> dict_def_2
		  
{'key1': 'value1', 'key2': 'value2'}
>>> type(dict_def_2)
		  
<class 'dict'>
>>> #dict_def_2 is a data-typed mapped dictionary from list to dict data-type.
		  
>>> dict_def_2 = dict([('key1','value1','key3','value3'),('key2','value2')])
		  
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dict_def_2 = dict([('key1','value1','key3','value3'),('key2','value2')])
ValueError: dictionary update sequence element #0 has length 4; 2 is required
>>> #ValueError here describes that first element has 4 elements or is of length
		  
>>> #4 but only 2 is required.
		  
>>> 'key1' in dict_def_2
		  
True
>>> #returns True signifying 'key1' is a key present in dict_def_2.
		  
>>> sorted(dict_def_2.keys())
		  
['key1', 'key2']
>>> sorted(dict_def_2.keys(),reverse=True)
		  
['key2', 'key1']
>>> #when reverse is True, sorting is done in descending order else by
		  
>>> #default sorted function has reverse=False, means sorting in ascending.
		  
>>> reverse(dict_def_2.keys())
		  
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    reverse(dict_def_2.keys())
NameError: name 'reverse' is not defined
>>> dict_def_2.get('key1')
		  
'value1'
>>> #get() method/attribute of dict is used to retrieve value of a key in a dict
		  
>>> help()
		  

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> get()
No Python documentation found for 'get()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> dict.get()
No Python documentation found for 'dict.get()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> dict
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> dict_def_2.getitem('key1')
		  
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict_def_2.getitem('key1')
AttributeError: 'dict' object has no attribute 'getitem'
>>> dict_def_2.__getitem__('key1')
		  
'value1'
>>> dict_def_2.__setitem__('key1') = 'value1 changed'
		  
SyntaxError: can't assign to function call
>>> dict_def_2.__setitem__('key1')
		  
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    dict_def_2.__setitem__('key1')
TypeError:  expected 2 arguments, got 1
>>> dict_def_2.__setitem__('key1','value1 changed')
		  
>>> dict_def_2.__getitem__('key1')
		  
'value1 changed'
>>> dict_def_2
		  
{'key1': 'value1 changed', 'key2': 'value2'}
>>> dict_def_2.__ge__('value2')
		  
NotImplemented
>>> dict_def_2.__ge__()
		  
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dict_def_2.__ge__()
TypeError: expected 1 arguments, got 0
>>> dict_def_2.__ge__('key2')
		  
NotImplemented
>>> 
