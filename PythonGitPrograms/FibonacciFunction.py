def fibonacci():
    first_number=0
    second_number=1
    end_number=int(input('Enter last number:\t'))
    while(first_number<=end_number):
        print(first_number)
        first_number, second_number=second_number, first_number+second_number
fibonacci()
