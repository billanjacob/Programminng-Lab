Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = float(input("Enter first number: "))

Enter first number: 4
>>> b= float(input("Enter first number: "))

Enter first number: 6
>>> c = float(input("Enter first number: "))

Enter first number: 1
>>> if (a > b) and (a > c):
	biggest = a
elif (b > a) and (b > c):
	biggest = b
else:
   biggest = c

   
>>> print("The biggest number is",biggest)
The biggest number is 6.0
>>> 