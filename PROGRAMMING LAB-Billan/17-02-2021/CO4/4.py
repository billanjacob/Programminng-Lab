class a:

    def __init__(self,h=0,m=0,s=0):
        self.__hour=h
        self.__minute=m
        self.__second=s

    def __add__(self,other):
        second=int((self.__second + other.__second)%60)
        minute=int((self.__minute + other.__minute)%60 + ((self.__second + other.__second)/60))
        hour=int((self.__hour + other.__hour)%24 + (self.__minute + other.__minute)/60)

        print('Time1 - ',self.__hour,':',self.__minute,':',self.__second)
        print('Time2 - ', other.__hour, ':', other.__minute, ':', other.__second)
        print('Toal time - ',hour,':',minute,':',second)

ob1=a(6,18,43)
ob2=a(2,34,23)

ob1+ob2