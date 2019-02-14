import threading
import time

def my_for_loop(number):
	sum = 0
	for i in range(number):
		sum = sum + i
	print ('My Name is Aman Raparia')
	
	
if __name__ == '__main__':
	
	t1 = threading.Thread(target=my_for_loop, args=(250000,))
	t2 = threading.Thread(target=my_for_loop, args=(250000,))
	
	start_time = time.time()
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
	print (f'total time taken is {time.time()-start_time})')