Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def func(string):
	length = len(string)
	if length>1:
		if string[-3:]=='ing':
			string=string+'ly'
		else:
			string=string+'ing'
	return string

>>> print(func('python'))
pythoning
>>> print(func('walking'))
walkingly
>>> 