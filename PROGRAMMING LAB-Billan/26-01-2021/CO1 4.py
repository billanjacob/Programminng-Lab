Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def count(str):
	d = dict()
	words = str.split()
	for word in words:
		if word in d:
			d[word] += 1
		else:
			d[word] = 1
	return d

>>> print(count('this is a python program to count the occurrences of each word in a line of text'))
{'this': 1, 'is': 1, 'a': 2, 'python': 1, 'program': 1, 'to': 1, 'count': 1, 'the': 1, 'occurrences': 1, 'of': 2, 'each': 1, 'word': 1, 'in': 1, 'line': 1, 'text': 1}
>>> 