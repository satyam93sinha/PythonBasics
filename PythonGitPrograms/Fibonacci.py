def fib(n):
    print("Fibonacci series:")
    a=0
    b=1
    temp=0
    print(a,"\n",b)
    while(a<n):
        temp=b
        b=a+b
        print(a)
        a=temp
def fibonacci(n):
    #returns Fibonacci series upto n
    """Creates a list of fibonacci series than directly printing it"""
    a,b=0,1
    #multiple variable assignment
    result=[]
    #list named result declared, an empty list.
    while(a<n):
    #checks condition
        result.append(a)
    #append method accessed by list's object result, it adds value to list.
    #printing or appending variable a lets ouput be less than n whereas
    #appending b would let output on interpreter depict number of iterations.
        a,b=b,a+b
    #multiple assignment, evaluates right side first from left to right then assigns.
    return result
