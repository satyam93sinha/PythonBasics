import multiprocessing
import time
def square_calculate(numbers_list):
	for number in numbers_list:
		print (f'Square of {number} is {number**2}')
		
def even_calculate(numbers_list):
	for number in numbers_list:
		if number%2 == 0:
			print (f'{number} is even')
			
#if __name__ == '__main__':
numbers_list = [1,56, 35, 23, 28, 55, 20, 47, 16,72]
	
start_time = time.time()
	#square_calculate(numbers_list)
p1 = multiprocessing.Process(target = square_calculate, args = (numbers_list[:5],))
p2 = multiprocessing.Process(target = square_calculate, args = (numbers_list[5:],))
	
p1start()
p2.start()
	
p1.join()
p2.join()
	
	
print (f'total time taken is {time.time()-start_time}')
	