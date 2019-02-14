Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f = open('file4.txt', 'w')
>>> f.write(123)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    f.write(123)
TypeError: write() argument must be str, not int
>>> f.write('123')
3
>>> f.read()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    f.read()
io.UnsupportedOperation: not readable
>>> f.close()
>>> f.closed
True
>>> f = open('file4.txt')
>>> f.read()
'123'
>>> int(f.read())
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    int(f.read())
ValueError: invalid literal for int() with base 10: ''
>>> x = int(f.read())
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x = int(f.read())
ValueError: invalid literal for int() with base 10: ''
>>> int('123')
123
>>> import json
>>> x=json.load(f)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x=json.load(f)
  File "G:\Softwares\Python 3.7.0\lib\json\__init__.py", line 296, in load
    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "G:\Softwares\Python 3.7.0\lib\json\__init__.py", line 348, in loads
    return _default_decoder.decode(s)
  File "G:\Softwares\Python 3.7.0\lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "G:\Softwares\Python 3.7.0\lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
>>> x=json.load(f.read())
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x=json.load(f.read())
  File "G:\Softwares\Python 3.7.0\lib\json\__init__.py", line 293, in load
    return loads(fp.read(),
AttributeError: 'str' object has no attribute 'read'
>>> dir(json)
		 
['JSONDecodeError', 'JSONDecoder', 'JSONEncoder', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_default_decoder', '_default_encoder', 'codecs', 'decoder', 'detect_encoding', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']
>>> print(json.__doc__)
		 
JSON (JavaScript Object Notation) <http://json.org> is a subset of
JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data
interchange format.

:mod:`json` exposes an API familiar to users of the standard library
:mod:`marshal` and :mod:`pickle` modules.  It is derived from a
version of the externally maintained simplejson library.

Encoding basic Python object hierarchies::

    >>> import json
    >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    '["foo", {"bar": ["baz", null, 1.0, 2]}]'
    >>> print(json.dumps("\"foo\bar"))
    "\"foo\bar"
    >>> print(json.dumps('\u1234'))
    "\u1234"
    >>> print(json.dumps('\\'))
    "\\"
    >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
    {"a": 0, "b": 0, "c": 0}
    >>> from io import StringIO
    >>> io = StringIO()
    >>> json.dump(['streaming API'], io)
    >>> io.getvalue()
    '["streaming API"]'

Compact encoding::

    >>> import json
    >>> mydict = {'4': 5, '6': 7}
    >>> json.dumps([1,2,3,mydict], separators=(',', ':'))
    '[1,2,3,{"4":5,"6":7}]'

Pretty printing::

    >>> import json
    >>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
    {
        "4": 5,
        "6": 7
    }

Decoding JSON::

    >>> import json
    >>> obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
    >>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
    True
    >>> json.loads('"\\"foo\\bar"') == '"foo\x08ar'
    True
    >>> from io import StringIO
    >>> io = StringIO('["streaming API"]')
    >>> json.load(io)[0] == 'streaming API'
    True

Specializing JSON object decoding::

    >>> import json
    >>> def as_complex(dct):
    ...     if '__complex__' in dct:
    ...         return complex(dct['real'], dct['imag'])
    ...     return dct
    ...
    >>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
    ...     object_hook=as_complex)
    (1+2j)
    >>> from decimal import Decimal
    >>> json.loads('1.1', parse_float=Decimal) == Decimal('1.1')
    True

Specializing JSON object encoding::

    >>> import json
    >>> def encode_complex(obj):
    ...     if isinstance(obj, complex):
    ...         return [obj.real, obj.imag]
    ...     raise TypeError(f'Object of type {obj.__class__.__name__} '
    ...                     f'is not JSON serializable')
    ...
    >>> json.dumps(2 + 1j, default=encode_complex)
    '[2.0, 1.0]'
    >>> json.JSONEncoder(default=encode_complex).encode(2 + 1j)
    '[2.0, 1.0]'
    >>> ''.join(json.JSONEncoder(default=encode_complex).iterencode(2 + 1j))
    '[2.0, 1.0]'


Using json.tool from the shell to validate and pretty-print::

    $ echo '{"json":"obj"}' | python -m json.tool
    {
        "json": "obj"
    }
    $ echo '{ 1.2:3.4}' | python -m json.tool
    Expecting property name enclosed in double quotes: line 1 column 3 (char 2)

>>> f.read()
		 
''
>>> f.close()
		 
>>> f = open('file4.txt', 'w')
		 
>>> x = {1:1, 2:4}
		 
>>> import json
		 
>>> json.dump(x, f)
		 
>>> f.close()
		 
>>> f = open('file4.txt')
		 
>>> f.read()
		 
'{"1": 1, "2": 4}'
>>> # json.dump() converts any data-type to string and stores in file.
		 
>>> x = json.load(f)
		 
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x = json.load(f)
  File "G:\Softwares\Python 3.7.0\lib\json\__init__.py", line 296, in load
    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "G:\Softwares\Python 3.7.0\lib\json\__init__.py", line 348, in loads
    return _default_decoder.decode(s)
  File "G:\Softwares\Python 3.7.0\lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "G:\Softwares\Python 3.7.0\lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
>>> f.close()
>>> f = open('file4.txt')
>>> json.load(f)
{'1': 1, '2': 4}
>>> # in 'r' mode, default mode, json.load() loads file object in the way it
>>> # was written into file.
>>> f.close()
>>> f = open('file4.txt', 'w')
>>> x = 123
>>> json.dump(x, f)
>>> json.dumps(456)
'456'
>>> f.close()
>>> f = open('file4.txt', 'r+')
>>> f.read()
'123'
>>> json.load(f)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    json.load(f)
  File "G:\Softwares\Python 3.7.0\lib\json\__init__.py", line 296, in load
    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "G:\Softwares\Python 3.7.0\lib\json\__init__.py", line 348, in loads
    return _default_decoder.decode(s)
  File "G:\Softwares\Python 3.7.0\lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "G:\Softwares\Python 3.7.0\lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
>>> f.close()
>>> f = open('file4.txt', 'r')
>>> json.load(f)
123
>>> f.close()
>>> f = open('file4.txt', 'r+')
>>> json.load(f)
123
>>> # to put objects into file, use json.dump(), converts to str, saves to file
>>> # to retrieve same data type, use json.load()
>>> 
