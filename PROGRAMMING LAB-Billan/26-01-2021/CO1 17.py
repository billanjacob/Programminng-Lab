Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import operator
>>> d = {3:0,2:4,4:1,0:3}
>>> print ("Before sorting : ",d)
Before sorting :  {3: 0, 2: 4, 4: 1, 0: 3}
>>> sorteddic = sorted(d.items(), key=operator.itemgetter(1))
>>> print('Dictionary in ascending order by value : ',sorteddic)
Dictionary in ascending order by value :  [(3, 0), (4, 1), (0, 3), (2, 4)]
>>> sorteddic = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
>>> sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
>>> print('Dictionary in descending order by value : ',sorteddic)
Dictionary in descending order by value :  {2: 4, 0: 3, 4: 1, 3: 0}
>>> 