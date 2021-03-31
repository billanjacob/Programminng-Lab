class rectangle:

    def __init__(self,l,b):
        self.__length=l
        self.__breadth=b
        self.area = self.__length * self.__breadth

    #def area(self):
    #    return self.length*self.breadth

    def display(self,obj):
        print('Area of rectangle 1 : ',self.area)
        print('Area of rectangle 2 : ',obj.area)

    def __lt__(self, obj):
        if self.area>obj.area:
            print('First rectangle has larger area')
        elif self.area<obj.area:
            print('Second rectangle has larger area')
        else:
            print('Equal area')

l=float(input('Enter length of 1st rectangle: '))
b=float(input('Enter width of 1st rectangle: '))
ob1=rectangle(l,b)

l=float(input('Enter length of 2nd rectangle: '))
b=float(input('Enter width of 2nd rectangle: '))
ob2=rectangle(l,b)

ob1.display(ob2)
ob1<ob2