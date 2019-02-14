class Name:
    def __init__ (self,name):
        self.name=name
class FullName(Name):
    def __init__(self,name):
        super().__init__(name)
        self.name='name'+'blank'

f=FullName('Vartika')
print(f.name)
#super() in inheritance, mro works when there is same named function. MRO?
