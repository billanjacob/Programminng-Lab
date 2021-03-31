Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Merge(d1,d2):
	return(d2.update(d1))

>>> d1 = {'a': 5, 'b': 2}
>>> d2 = {'g': 7, 'e': 1}
>>> print(Merge(d1, d2))
None
>>> print(d2)
{'g': 7, 'e': 1, 'a': 5, 'b': 2}
>>> 