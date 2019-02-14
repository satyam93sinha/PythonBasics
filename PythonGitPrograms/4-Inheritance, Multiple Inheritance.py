Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Polygon:
	def __init__(self, no_of_sides):
		self.n = no_of_sides
		self.sides = [0 for i in range(no_of_sides)]
	def input_sides(self):
	        self.sides = [float(input("Enter sides {}:".format(i+1))) for i in range(self.n)]
	def display_sides(self):
		print(self.sides)

		
>>> pol = Polygon(3)
>>> pol.input_sides
<bound method Polygon.input_sides of <__main__.Polygon object at 0x0302C8B0>>
>>> # returns the memory location of particular method object
>>> Polygon.input_sides(Polygon)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Polygon.input_sides(Polygon)
  File "<pyshell#9>", line 6, in input_sides
    self.sides = [float(input("Enter sides {}:".format(i+1))) for i in range(self.n)]
AttributeError: type object 'Polygon' has no attribute 'n'
>>> # I need the instance object to refer to n, which wasn't provided.
>>> class Triangle(Polygon):
	def __init__(self):
		super().__init__(3)
	def perimeter(self):
		self.perim = 0
		for i in self.sides:
			self.perim += i
		print(self.perim)

		
>>> t = Triangle()
>>> t.input_sides()
Enter sides 1:3
Enter sides 2:4
Enter sides 3:5
>>> t.display_sides()
[3.0, 4.0, 5.0]
>>> t.perimeter()
12.0
>>> # I was able to access input_sides() bcoz I provided exactly the number of
>>> # arguments it needed, instantiating its parent class to have sides.n
>>> # and other objects.
>>> class Triangle2(Polygon, Triangle):
	def __init__(self):
		super().__init__(3)
	def area(self):
		s = self.perim/2
		a, b, c = self.sides
		ar = (s*(s-a)*(s-b)*(s-c)) ** 0.5
		print(ar)

		
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    class Triangle2(Polygon, Triangle):
TypeError: Cannot create a consistent method resolution
order (MRO) for bases Polygon, Triangle
>>> class Triangle2(Polygon, Triangle):
	def __init__(self):
		Triangle.__init__(Triangle, 3)
	def area(self):
		s = self.perim/2
		a, b, c = self.sides
		ar = (s*(s-a)*(s-b)*(s-c)) ** 0.5
		print(ar)

		
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    class Triangle2(Polygon, Triangle):
TypeError: Cannot create a consistent method resolution
order (MRO) for bases Polygon, Triangle
>>> class Triangle2(Triangle, Polygon):
	def __init__(self):
		super().__init__()
		super().__init__(3)
	def area(self):
		s = self.perim/2
		a, b, c = self.sides
		ar = (s*(s-a)*(s-b)*(s-c)) ** 0.5
		print(ar)

		
>>> 
>>> print(Triangle2.mro())
[<class '__main__.Triangle2'>, <class '__main__.Triangle'>, <class '__main__.Polygon'>, <class 'object'>]
>>> t2 = Triangle2()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    t2 = Triangle2()
  File "<pyshell#44>", line 4, in __init__
    super().__init__(3)
TypeError: __init__() takes 1 positional argument but 2 were given
>>> class Triangle2(Triangle, Polygon):
	def __init__(self):
		super().__init__()
		# super().__init__(3)
	def area(self):
		s = self.perim/2
		a, b, c = self.sides
		ar = (s*(s-a)*(s-b)*(s-c)) ** 0.5
		print(ar)

		
>>> t2 = Triangle2()
>>> t2.input_sides()
Enter sides 1:5
Enter sides 2:8
Enter sides 3:9
>>> t2.perimeter()
22.0
>>> t2.area()
19.8997487421324
>>> t2.display_sides()
[5.0, 8.0, 9.0]
>>> # we had already invoked super().__init__(3) in Triangle class, so invoking
>>> # again passed two arguments thus, received TypeError
>>> class Polygon:
	def __init__(self, no_of_sides):
		self.n = no_of_sides
		self.sides = [0 for i in range(no_of_sides)]
	def input_sides(self):
	        self.sides = [float(input("Enter sides {}:".format(i+1))) for i in range(self.n)]
	def display_sides(self):
		print(self.sides)
	def perimeter(self):
		self.peri = 0
		for i in range(self.n):
			self.peri += i
		print(self.peri)

		
>>> pol = Polygon(4)
>>> class Square(Polygon):
	def __init__(self):
		super().__init__(4)
	def area(self):
		if(self.sides[0] == self.sides[1] == self.sides[2]==self.sides[3]):
			print(self.sides[0]*self.sides[3])

			
>>> sq = Square()
>>> sq.input_sides()
Enter sides 1:4
Enter sides 2:4
Enter sides 3:4
Enter sides 4:4
>>> sq.display_sides()
[4.0, 4.0, 4.0, 4.0]
>>> sq.perimeter()
6
>>> sq.area()
16.0
>>> # perimeter is wrong bcoz logic is wrong.
>>> print(Triangle2.mro())
[<class '__main__.Triangle2'>, <class '__main__.Triangle'>, <class '__main__.Polygon'>, <class 'object'>]
>>> # looks into a class only once, first searches in derived class Triangle2,
>>> # then in Triangle base class, further in its base class or left-to-right
>>> # if base class of Triangle and Triangle2 are same, later in the end
>>> # searches in Object class.
>>> print(t.mro())
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    print(t.mro())
AttributeError: 'Triangle' object has no attribute 'mro'
>>> # bcoz t is an object of Triangle class
>>> print(t2.mro())
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print(t2.mro())
AttributeError: 'Triangle2' object has no attribute 'mro'
>>> # there's no attribute as mro() in Triangle2 or Triangle class.
>>> dir(t2)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'display_sides', 'input_sides', 'n', 'perim', 'perimeter', 'sides']
>>> dir(Triangle2)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'display_sides', 'input_sides', 'perimeter']
>>> 
