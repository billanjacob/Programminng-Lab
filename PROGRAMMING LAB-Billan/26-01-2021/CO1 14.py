Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input("Enter the integer : "))
Enter the integer : 7
>>> n1 = int("%s"%num)
>>> n2 = int("%s%s"%(num,num))
>>> n3 = int("%s%s%s"%(num,num,num))
>>> print(n1+n2+n3)
861
>>> 