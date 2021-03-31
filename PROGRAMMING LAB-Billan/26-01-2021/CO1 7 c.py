Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [2,5,9,12,49]
>>> list2 = [9,53,1,0]
>>> for i in list1:
	if i in list2:
		flag=1
		break
	else:
		flag=0

		
>>> if flag==1:
	print("there are common values")
else:
	print("there are no common values")

	
there are common values
>>> 