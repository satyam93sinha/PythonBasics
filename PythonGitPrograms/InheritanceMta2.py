class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,empID,CompanyName, name, age):
        Person.__init__(self,name,age)
        self.empID=empID
        self.CompanyName=CompanyName

ob=Employee(202,'M', 'Aman', 24)
print (issubclass(Employee, Person))
#print (ob.__mro__)
print(Employee.__mro__)
