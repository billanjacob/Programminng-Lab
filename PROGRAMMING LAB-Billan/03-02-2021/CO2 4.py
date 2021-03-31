Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def fun():
	for i in range(2000,15000):
		sqroot = int(math.sqrt(i))
		string = str(i)
		n1=int(string[0])
		n2=int(string[1])
		n3=int(string[2])
		n4=int(string[3])
		if(sqroot*sqroot==i):
			if((n1%2==0)and(n2%2==0)and(n3%2==0)and(n4%2==0)):
				print(i)

				
>>> fun()
4624
6084
6400
8464
>>> 