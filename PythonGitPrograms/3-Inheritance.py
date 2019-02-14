Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Polygon:
	def __init__(self, no_of_sides)
	
SyntaxError: invalid syntax
>>> class Polygon:
	def __init__(self, no_of_sides):
		self.n = no_of_sides
		self.sides = [0 for i in range(self.n)]
	def input_sides(self):
		self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
	def display_sides(self):
		for i in range(self.n):
			print("Sides: {} is : {}
			      
SyntaxError: EOL while scanning string literal
>>> class Polygon:
	def __init__(self, no_of_sides):
		self.n = no_of_sides
		self.sides = [0 for i in range(self.n)]
	def input_sides(self):
		self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
	def display_sides(self):
		for i in range(self.n):
			print("Sides: {} is : {}".format(i+1, self.sides[i]))

			      
>>> pol = Polygon(4)
			      
>>> pol.input_sides()
			      
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    pol.input_sides()
  File "<pyshell#11>", line 6, in input_sides
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
  File "<pyshell#11>", line 6, in <listcomp>
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
TypeError: input expected at most 1 arguments, got 2
>>> pol.input_sides
			      
<bound method Polygon.input_sides of <__main__.Polygon object at 0x03291D90>>
>>> # when we invoke input_sides() through instance object, it already has
			      
>>> # two arguments, i.e, Polygon(self, 4), thus mentions TypeError above.
			      
>>> Polygon.input_sides(Polygon)
			      
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    Polygon.input_sides(Polygon)
  File "<pyshell#11>", line 6, in input_sides
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
AttributeError: type object 'Polygon' has no attribute 'n'
>>> Polygon.display_sides(Polygon)
			      
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    Polygon.display_sides(Polygon)
  File "<pyshell#11>", line 8, in display_sides
    for i in range(self.n):
AttributeError: type object 'Polygon' has no attribute 'n'
>>> pol.display_sides
			      
<bound method Polygon.display_sides of <__main__.Polygon object at 0x03291D90>>
>>> # the functions are already bound
			      
>>> class Triangle(Polygon):
	def __init__(self):
	    super().__init__(3)

			      
>>> t = Triangle()
			      
>>> t.input_sides()
			      
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    t.input_sides()
  File "<pyshell#11>", line 6, in input_sides
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
  File "<pyshell#11>", line 6, in <listcomp>
    self.sides = [float(input("Enter sides:", str(i+1))) for i in range(self.n)]
TypeError: input expected at most 1 arguments, got 2
>>> t.display_sides()
			      
Sides: 1 is : 0
Sides: 2 is : 0
Sides: 3 is : 0
>>> class Polygon:
	def __init__(self, no_of_sides):
		self.n = no_of_sides
		self.sides = [0 for i in range(self.n)]
	def input_sides(self):
		self.sides = [float(input("Enter sides: '+str(i+1)+' :")) for i in range(self.n)]
	def display_sides(self):
		for i in range(self.n):
			print("Sides: {} is : {}".format(i+1, self.sides[i]))

			      
>>> pol = Polygon(4)
			      
>>> class Triangle(Polygon):
	def __init__(self):
	    super().__init__(3)

			      
>>> t = Triangle()
			      
>>> t.input_sides()
			      
Enter sides: '+str(i+1)+' :2
Enter sides: '+str(i+1)+' :4
Enter sides: '+str(i+1)+' :5
>>> t.display_sides()
			      
Sides: 1 is : 2.0
Sides: 2 is : 4.0
Sides: 3 is : 5.0
>>> # seems print('string', str) works in this only, in input('Enter sides' +str
			      
>>> # (i+1)) converts i+1 int to str bcoz input takes str then to float.
			      
>>> # This was the issue, we kept getting earlier.
			      
>>> # Thus, one of the method is this
			      
>>> 
