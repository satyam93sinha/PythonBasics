def parent():
    def child1():
        print ('I am child1')
    def child2():
        print("I am child2")
    return child1()
    child2()
parent()
