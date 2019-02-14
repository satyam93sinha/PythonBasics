Python 3.6.5rc1 (v3.6.5rc1:f03c5148cf, Mar 14 2018, 03:12:11) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> >>> def parrot(colour,sound="multiple sounds",fly='yes',species=393):
	print("Parrot is ",colour)
	print("Parrot can produce",sound,"comes from a family of ",species,"species")

SyntaxError: invalid syntax
>>> def parrot(colour,sound="multiple sounds",fly='yes',species=393):
	print("Parrot is ",colour)
	print("Parrot can produce",sound,"comes from a family of ",species,"species")

	
>>> parrot('Green')#1 required positional argument
Parrot is  Green
Parrot can produce multiple sounds comes from a family of  393 species
>>> def parrot(colour,sound="multiple sounds",fly='yes',species=393):
	print("Parrot is ",colour)
	print("Parrot can produce",sound,"comes from a family of ",species,"species")
	print(colour,sound,fly,species)

	
>>> parrot('Green','screaching qwack','fly is true','parrots species 393')
Parrot is  Green
Parrot can produce screaching qwack comes from a family of  parrots species 393 species
Green screaching qwack fly is true parrots species 393
>>> #We passed 4 positional arguments
>>> parrot(colour='Green',sound='mimicry',fly='true',species='393 parrot species')
Parrot is  Green
Parrot can produce mimicry comes from a family of  393 parrot species species
Green mimicry true 393 parrot species
>>> parrot(colour='Green',species='393 parrot species',fly='true',sound='mimicry')#1 positional argument followed by 3 keyword arguments passed randomly
Parrot is  Green
Parrot can produce mimicry comes from a family of  393 parrot species species
Green mimicry true 393 parrot species
>>> parrot(fly='true','green')#1 keyword argument followed by 1 positional argument passed randomly
SyntaxError: positional argument follows keyword argument
>>> 
