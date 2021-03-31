Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string = "pythonprogram"
>>> d = {}
>>> for i in string:
	key = d.keys()
	if i in key:
		d[i]=d[i]+1
	else:
		d[i]=1

		
>>> print(d)
{'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 1, 'r': 2, 'g': 1, 'a': 1, 'm': 1}
>>> 