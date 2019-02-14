class Car:
    wheels=4
    name='other'
    def __init__(self,**kwargs):
        if 'name' in kwargs:
            self.name=kwargs['name']

c=Car()
print(c.__dict__)
d=Car(name='Toyota')
print(d.__dict__)
print("car class dictionary",Car.__dict__)
# name and wheels are class variables, no argument was passed in function
# as it was optional dictionary. No instance variable was set,if condition
# turns out to be false because there's nothing in dictionary (nothing passed)
# Car.__dict__ would have returned a dictionary.
# In this program object is made but there isn't any instance variable so
# output is empty dictionary.

