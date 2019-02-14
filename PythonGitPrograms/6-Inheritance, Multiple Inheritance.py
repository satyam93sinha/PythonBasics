Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===== RESTART: G:/ProgramsPython/5-Inheritance, Multiple Inheritance.py =====
Base1, a:5, b:9
Base2, a:2, c:3
Child1, d:1, e:go
Child2
>>> ch = Child2()
>>> ch.a
2
>>> ch.mro()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    ch.mro()
AttributeError: 'Child2' object has no attribute 'mro'
>>> print(Child2.mro())
[<class '__main__.Child2'>, <class '__main__.Child1'>, <class '__main__.Base2'>, <class '__main__.Base1'>, <class 'object'>]
>>> print(Child2.mro(), ch.a, Child2.mro())
[<class '__main__.Child2'>, <class '__main__.Child1'>, <class '__main__.Base2'>, <class '__main__.Base1'>, <class 'object'>] 2 [<class '__main__.Child2'>, <class '__main__.Child1'>, <class '__main__.Base2'>, <class '__main__.Base1'>, <class 'object'>]
>>> print(Child2.mro(), ch.b, Child2.mro())
[<class '__main__.Child2'>, <class '__main__.Child1'>, <class '__main__.Base2'>, <class '__main__.Base1'>, <class 'object'>] 9 [<class '__main__.Child2'>, <class '__main__.Child1'>, <class '__main__.Base2'>, <class '__main__.Base1'>, <class 'object'>]
>>> 
===== RESTART: G:/ProgramsPython/5-Inheritance, Multiple Inheritance.py =====
Base1, a:5, b:9
Traceback (most recent call last):
  File "G:/ProgramsPython/5-Inheritance, Multiple Inheritance.py", line 4, in <module>
    class Base2:
  File "G:/ProgramsPython/5-Inheritance, Multiple Inheritance.py", line 5, in Base2
    print("Base2.mro:{}".format(Base2.mro()))
NameError: name 'Base2' is not defined
>>> 
===== RESTART: G:/ProgramsPython/5-Inheritance, Multiple Inheritance.py =====
Base1, a:5, b:9
Base2, a:2, c:3
Traceback (most recent call last):
  File "G:/ProgramsPython/5-Inheritance, Multiple Inheritance.py", line 8, in <module>
    class Child1(Base2):
  File "G:/ProgramsPython/5-Inheritance, Multiple Inheritance.py", line 9, in Child1
    print("Child1.mro:{}".format(Child1.mro()))
NameError: name 'Child1' is not defined
>>> 
===== RESTART: G:/ProgramsPython/5-Inheritance, Multiple Inheritance.py =====
Base1, a:5, b:9
Base2, a:2, c:3
Child1, d:1, e:go
Child2
Traceback (most recent call last):
  File "G:/ProgramsPython/5-Inheritance, Multiple Inheritance.py", line 11, in <module>
    class Child2(Child1, Base2, Base1):
  File "G:/ProgramsPython/5-Inheritance, Multiple Inheritance.py", line 13, in Child2
    print("Child2.mro():{}".format(Child2.mro()))
NameError: name 'Child2' is not defined
>>> 
===== RESTART: G:/ProgramsPython/5-Inheritance, Multiple Inheritance.py =====
Base1, a:5, b:9
Base2, a:2, c:3
Child1, d:1, e:go
Child2
Child2.mro():[<class '__main__.Child2'>, <class '__main__.Child1'>, <class '__main__.Base2'>, <class '__main__.Base1'>, <class 'object'>]
Child1.mro:[<class '__main__.Child1'>, <class '__main__.Base2'>, <class 'object'>]
>>> # Unless class is executed we can't have its object or instance thus we got
>>> # NameError, later it seems mro() stays static, same here in every call.
>>> 
