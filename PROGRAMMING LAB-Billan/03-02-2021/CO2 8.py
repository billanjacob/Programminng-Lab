Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def func(word):
	l=[]
	for i in word:
		l.append((len(i),i))
	l.sort()
	length=l[-1][0]
	lword=l[-1][1]
	print("Longest word : ",lword)
	print("Length : ",length)

	
>>> func(['one','two','three','four'])
Longest word :  three
Length :  5
>>> 