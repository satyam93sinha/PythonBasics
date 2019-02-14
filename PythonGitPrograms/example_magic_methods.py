class Vector:
	def __init__(self, *args):
		if len(args) == 0:
			self.values = (0,0)
		else:
			self.values = args
	def __add__(self, others):
		result = tuple([self.values[0] + others.values[0],
						self.values[1] + others.values[1]])
		a, b = result
		obj = Vector(a,b)
		return obj
a1 = Vector(1,3)
a2 = Vector(2,3)
result = a1 + a2
a = 1 + 2
print (a)
print (result.values)  
print (a1.values)
print (a2.values)
print (type(Vector))
print (type(int))