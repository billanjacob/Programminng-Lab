Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=int(input("enter the side of square : "))
enter the side of square : 4
>>> area=lambda a:a*a
>>> print(area(s))
16
>>> l=int(input("enter length : "))
enter length : 7
>>> b=int(input("enter breadth : "))
enter breadth : 3
>>> area=lambda l,b:l*b
>>> print(area(l,b))
21
>>> h=int(input("Enter height of triangle : "))
Enter height of triangle : 8
>>> b=int(input("enter base of triangle : "))
enter base of triangle : 4
>>> area=lambda h,b1:(l*b1)/2
>>> print(area(h,b))
14.0
>>> 