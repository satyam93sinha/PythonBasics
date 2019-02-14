class Base1:
    a, b = 5, 9
    print('Base1, a:{}, b:{}'.format(a, b))
class Base2:
    #print("Base2.mro:{}".format(Base2.mro()))
    a, c = 2, 3
    print("Base2, a:{}, c:{}".format(a, c))
class Child1(Base2):
    d, e = 1, 'go'
    print("Child1, d:{}, e:{}".format(d, e))
class Child2(Child1, Base2, Base1):
    print("Child2")

print("Child2.mro():{}".format(Child2.mro()))

print("Child1.mro:{}".format(Child1.mro()))
