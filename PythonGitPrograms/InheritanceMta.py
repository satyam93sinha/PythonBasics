class Person:
    def __init__(self,name,age):
        self.__name=name
        self.age=age
class Employee(Person):
    def __init__(self,empID,CompanyName, name, age):
        super().__init__(name,age)
        self.__name = name
        self.empID=empID
        self.CompanyName=CompanyName

ob=Employee(202,'M', 'Aman', 24)
print (issubclass(Employee, Person))
ob._Employee__name = 'Suresh'
print (ob._Employee__name)
