Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list=[8,9,3,2]
>>> print("Before removal : ",list)
Before removal :  [8, 9, 3, 2]
>>> for i  in list:
	if(i%2 == 0):
		list.remove(i)

		
>>> print("After removing even numbers : ",list)
After removing even numbers :  [9, 3]
>>> 