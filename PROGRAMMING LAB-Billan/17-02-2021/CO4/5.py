class publisher:
    def __init__(self,n):
        self.name=n
    def show(self):
        pass

class book(publisher):
    def __init__(self,t,a,n):
        self.title=t
        self.author=a
        publisher.__init__(self,n)
    def show(self):
        pass

class python(book):
    def __init__(self,p,no,t,a,n):
        self.price=p
        self.no_of_pages=no
        book.__init__(self,t,a,n)
    def show(self):
        print('Book title:',self.title)
        print('Author:',self.author)
        print('Publisher:',self.name)
        print('Price: Rs.',self.price)
        print('No of pages:',self.no_of_pages)

obj=python(3125,600,'Python- The Complete Reference','Martin Brown','Osborne')
obj.show()