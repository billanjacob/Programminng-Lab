Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def gcd(a,b):
	if (b == 0):
		return a
	return gcd(b, a%b)

>>> a=25
>>> b=14
>>> if(gcd(a, b)):
	print("GCD is", gcd(a, b))
else:
    print("GCD not found")

    
GCD is 1
>>> 