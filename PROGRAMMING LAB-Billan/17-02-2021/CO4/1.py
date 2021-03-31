class rectangle:

    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

    def display(self,obj):
        print('Area of rectangle 1 : ',self.area())
        print('Area of rectangle 2 : ',obj.area())
        print('Perimeter of rectangle 1 : ', self.perimeter())
        print('Perimeter of rectangle 2 : ', obj.perimeter())

    def compare(self,obj):
        if self.area()>obj.area():
            print('First rectangle has larger area')
        elif self.area()<obj.area():
            print('Second rectangle has larger area')
        else:
            print('Equal area')

ob1=rectangle(5,4)
ob2=rectangle(12,2)
ob1.display(ob2)
ob1.compare(ob2)
