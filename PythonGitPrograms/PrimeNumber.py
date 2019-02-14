#Using factor method to check if any number has any factors, if not its prime.
for i in range(185,192):
	for j in range(2,i):
		if (i%j==0):
			print(i,"equals",j,"*",i//j)
			break;
	else:
		print(i, "is a prime number")
#Using square-root method

	    
