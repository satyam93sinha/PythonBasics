Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: G:\ProgramsPython\1-Private Variables.py =============
>>> mapp = Mapping([2,4,6])
>>> mapp.item_list
[2, 4, 6]
>>> mapp.update
<bound method Mapping.update of <__main__.Mapping object at 0x02F6EED0>>
>>> mapp.update()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    mapp.update()
TypeError: update() missing 1 required positional argument: 'iterable'
>>> child = Child({1:1, 2:4})
>>> child.item_list
[1, 2]
>>> # invokes __update of Mapping class
>>> # this is known as only the keys get appended to item_list wch could happen
>>> # only if __update of Mapping class is invoked.
>>> child.update({1:1, 3:9})
>>> child.item_list
[1, 2, {1: 1}, {3: 9}]
>>> # for invoking update function of Child class we would need to pass
>>> # the argument in update function, it expects an argument.
