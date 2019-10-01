def fibo(n):  #defines function  and passes the value of n
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
        
n=input('enter the number of series you want') # n is the number of series 
if n<0:
    print 'invalid number' #if n is negative or less than n then it prints invalid input
for i in range(n):   #using loop to print series
    print fibo(i)  # calls fibo function and calls again till the loop is terminated
