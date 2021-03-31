Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def area(r):
	pi=3.14
	return pi*r*r

>>> radius=float(input("Enter the radius: "))
Enter the radius: 2
>>> a=area(radius)
>>> print("Area is:",a,"sq.units")
Area is: 12.56 sq.units
>>> 