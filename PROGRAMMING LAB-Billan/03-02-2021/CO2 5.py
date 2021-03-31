Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=int(input("Enter the limit : "))
Enter the limit : 5
>>> for i in range(1,l+1):
	j=1
	for j in range(1,i+1):
		temp=i*j
		print(temp,end="  ")
	print("")

	
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
>>> 