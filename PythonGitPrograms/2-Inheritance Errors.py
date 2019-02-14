Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Base:
	def __init__(self, string):
		string = 'Base class'
		return (string)
	def func_1(self, string1):
		self.string1 = string
		return(string1)

>>> base = Base()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    base = Base()
TypeError: __init__() missing 1 required positional argument: 'string'
>>> base = Base('Base')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    base = Base('Base')
TypeError: __init__() should return None, not 'str'
>>> class Base:
	def __init__(self, string):
		string = 'Base class'
		print (string)
	def func_1(self, string1):
		self.string1 = string
		return(string1)

	
>>> base = Base('Base')
Base class
>>> base.func_1
<bound method Base.func_1 of <__main__.Base object at 0x03491150>>
>>> base.func_1()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    base.func_1()
TypeError: func_1() missing 1 required positional argument: 'string1'
>>> base.func_1('Base again')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    base.func_1('Base again')
  File "<pyshell#10>", line 6, in func_1
    self.string1 = string
NameError: name 'string' is not defined
>>> class Base:
	def __init__(self, string):
		string = 'Base class'
		print (string)
	def func_1(self):
		self.string = 'Base function'
		return(string1)

	
>>> base = Base("Base")
Base class
>>> base.func_1()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    base.func_1()
  File "<pyshell#16>", line 7, in func_1
    return(string1)
NameError: name 'string1' is not defined
>>> class Base:
	def __init__(self, string):
		string = 'Base class'
		print (string)
	def func_1(self):
		self.string = 'Base function'
		return(string)

	
>>> base = Base("Base")
Base class
>>> base.func_1()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    base.func_1()
  File "<pyshell#20>", line 7, in func_1
    return(string)
NameError: name 'string' is not defined
>>> class Base:
	def __init__(self, string):
		self.string = 'Base class'
		print (self.string)

>>> base = Base('base')
Base class
>>> class Base:
	def __init__(self, string):
		self.string = 'Base class'
		print (self.string)
	def func_1(self):
		self.string = 'Base function'
		return(self.string)

	
>>> base = Base('base')
Base class
>>> base.func_1()
'Base function'
>>> class Base:
	def __init__(self, string):
		self.string = 'Base class'
		print (self.string)
	def func_1(self):
		self.string = 'Base function'
		print(self.string)
	self.func_1()

	
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    class Base:
  File "<pyshell#31>", line 8, in Base
    self.func_1()
NameError: name 'self' is not defined
>>> class Polygon:
	def __init__(self, no_of_sides):
		self.n = no_of_sides
		self.sides = [0 for i in range(no_of_sides)]
		print(self.n, self.sides)

		
>>> polygon = Polygon()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    polygon = Polygon()
TypeError: __init__() missing 1 required positional argument: 'no_of_sides'
>>> polygon = Polygon(4)
4 [0, 0, 0, 0]
>>> class Polygon1(Polygon):
	def input_sides(self):
		self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
		print(self.sides)

		
>>> pol = Polygon1()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    pol = Polygon1()
TypeError: __init__() missing 1 required positional argument: 'no_of_sides'
>>> pol = Polygon1(4)
4 [0, 0, 0, 0]
>>> pol.input_sides()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    pol.input_sides()
  File "<pyshell#45>", line 3, in input_sides
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
  File "<pyshell#45>", line 3, in <listcomp>
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
TypeError: input expected at most 1 arguments, got 2
>>> class Polygon1(Polygon):
	def __init__(self):
		print('Child constructor')
	def input_sides(self):
		self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
		print(self.sides)

		
>>> pol = Polygon1()
Child constructor
>>> pol.input_sides()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    pol.input_sides()
  File "<pyshell#50>", line 5, in input_sides
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
AttributeError: 'Polygon1' object has no attribute 'n'
>>> class Polygon1(Polygon):
	def __init__(self):
		print('Child constructor')
	def input_sides(self):
		self.sides = [float(input("Enter sides:", str(i+1))) for i in range(super(n))]
		print(self.sides)

		
>>> pol = Polygon1()
Child constructor
>>> pol.input_sides()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    pol.input_sides()
  File "<pyshell#54>", line 5, in input_sides
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(super(n))]
NameError: name 'n' is not defined
>>> # we have overridden constructor of base class, Polygon, so now we don't
>>> # have its attributes n and no_of_sides, thus we see NameError
>>> class Polygon1(Polygon):
	def __init__(self):
		super().__init__(4)
	def input_sides(self):
		self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
		print(self.sides)

		
>>> pol = Polygon1()
4 [0, 0, 0, 0]
>>> # now when instance object of Polygon1 is created, constructor of Polygon
>>> # class, base class, is also invoked.
>>> pol.input_sides()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    pol.input_sides()
  File "<pyshell#65>", line 5, in input_sides
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
  File "<pyshell#65>", line 5, in <listcomp>
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
TypeError: input expected at most 1 arguments, got 2
>>> pol.input_sides
<bound method Polygon1.input_sides of <__main__.Polygon1 object at 0x00C73A30>>
>>> pol.input_sides()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    pol.input_sides()
  File "<pyshell#65>", line 5, in input_sides
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
  File "<pyshell#65>", line 5, in <listcomp>
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
TypeError: input expected at most 1 arguments, got 2
>>> Polygon1.input_sides(Polygon1)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    Polygon1.input_sides(Polygon1)
  File "<pyshell#65>", line 5, in input_sides
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
AttributeError: type object 'Polygon1' has no attribute 'n'
>>> class Polygon1(Polygon):
	def __init__(self):
		super().__init__(4)
	def input_sides(self):
		self.sides = [float(input("Enter sides:", str(i+1))) for i in range(super().n)]
		print(self.sides)

		
>>> pol = Polygon1()
4 [0, 0, 0, 0]
>>> Polygon1.input_sides(Polygon1)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    Polygon1.input_sides(Polygon1)
  File "<pyshell#74>", line 5, in input_sides
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(super().n)]
AttributeError: 'super' object has no attribute 'n'
>>> class Polygon1(Polygon):
	def __init__(self):
		super().__init__(4)
	def input_sides(self):
		self.sides = [float(input("Enter sides:", str(i+1))) for i in range(super().__init__(4).n)]
		print(self.sides)

		
>>> pol = Polygon1()
4 [0, 0, 0, 0]
>>> Polygon1.input_sides(Polygon1)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    Polygon1.input_sides(Polygon1)
  File "<pyshell#78>", line 5, in input_sides
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(super().__init__(4).n)]
TypeError: __init__() missing 1 required positional argument: 'no_of_sides'
>>> class Polygon1(Polygon):
	def __init__(self):
		super().__init__(4)
	def input_sides(self):
		self.sides = [float(input("Enter sides:", str(i+1))) for i in range(Polygon.__init__(Polygon, 4).n)]
		print(self.sides)

		
>>> pol = Polygon1()
4 [0, 0, 0, 0]
>>> Polygon1.input_sides(Polygon1)
4 [0, 0, 0, 0]
Traceback (most recent call last):

  File "<pyshell#84>", line 1, in <module>
    Polygon1.input_sides(Polygon1)
  File "<pyshell#82>", line 5, in input_sides
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(Polygon.__init__(Polygon, 4).n)]
AttributeError: 'NoneType' object has no attribute 'n'
>>> 
