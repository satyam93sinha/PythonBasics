def fibonacci_return(input_num):
    print("fibonacci_return(input_num):")
    first_num = 0
    second_num = 1
    fibo_list = []
    #input_num = int(input('Series to be less or equal to:\t'))
    while(first_num <= input_num):
        fibo_list.append(first_num)
        #print(first_num)
        first_num, second_num=second_num, first_num+second_num
    return (fibo_list)
#print(list(fibonacci_return(num))
            
