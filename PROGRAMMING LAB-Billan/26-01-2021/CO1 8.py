Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def func(string):
	firstchar=string[0]
	string=string.replace(firstchar, '$')
	string=firstchar+string[1:]
	return string

>>> print(func("character"))
chara$ter
>>> 