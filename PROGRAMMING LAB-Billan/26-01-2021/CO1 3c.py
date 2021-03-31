Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string = "This is a python program"
>>> print ("The string is : ",string)
The string is :  This is a python program
>>> vowels = "AaEeIiOoUu"
>>> final = set([each for each in string if each in vowels])
>>> print ("Vowels present are : ",final)
Vowels present are :  {'a', 'o', 'i'}
>>> 