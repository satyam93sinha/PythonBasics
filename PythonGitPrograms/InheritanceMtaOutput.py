Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
>>> ob.__dict__
{'empID': 202, 'CompanyName': 'M'}
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
{'empID': 202, 'CompanyName': 'M'}
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
{'name': 'Aman', 'age': 24, 'empID': 202, 'CompanyName': 'M'}
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
Aman
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
Aman
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
Aman
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
Traceback (most recent call last):
  File "G:/Softwares/Python/InheritanceMta.py", line 13, in <module>
    print (ob.__mro__)
AttributeError: 'Employee' object has no attribute '__mro__'
>>> class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,empID,CompanyName, name, age):
        super().__init__(name,age)
        self.empID=empID
        self.CompanyName=CompanyName
        
SyntaxError: invalid syntax
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
Traceback (most recent call last):
  File "G:/Softwares/Python/InheritanceMta.py", line 13, in <module>
    print (ob.__mro__())
AttributeError: 'Employee' object has no attribute '__mro__'
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
Traceback (most recent call last):
  File "G:/Softwares/Python/InheritanceMta.py", line 13, in <module>
    print (ob.__MRO__)
AttributeError: 'Employee' object has no attribute '__MRO__'
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
Traceback (most recent call last):
  File "G:/Softwares/Python/InheritanceMta.py", line 13, in <module>
    print (ob.mro())
AttributeError: 'Employee' object has no attribute 'mro'
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
(<class '__main__.Employee'>, <class '__main__.Person'>, <class 'object'>)
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
(<class '__main__.Employee'>, <class '__main__.Person'>, <class 'object'>)
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
{'name': 'Aman', 'age': 24, 'empID': 202, 'CompanyName': 'M'}
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
{'_Person__name': 'Aman', 'age': 24, '_Employee__name': 'Aman', 'empID': 202, 'CompanyName': 'M'}
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
Aman
>>> 
=============== RESTART: G:/Softwares/Python/InheritanceMta.py ===============
True
Suresh
>>> 
