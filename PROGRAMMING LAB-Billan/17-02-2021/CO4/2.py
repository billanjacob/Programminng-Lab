class Account:

    def __init__(self,a,n,t,b):
        self.acno=a
        self.name=n
        self.type=t
        self.balance=b

    def deposit(self,a):
        self.balance+=a
        print('Rs.',a,'deposited. Current balance is: Rs.',self.balance)

    def withdraw(self,a):
        if self.balance >= a:
            self.balance -= a
            print('Rs.',a,'withdrawn. Current balance is: Rs.', self.bal)
        else:
            print('Insufficient balance to make this transaction.')

a = int(input('Enter account number:'))
n = input('Enter name of the account holder: ')
t = input('Enter account type: ')
b = float(input('Enter your balance:'))

obj = Account(a,n,t,b)
ch = '1'

while ch!='4':
    print('1.Deposit')
    print('2.Withdraw')
    print('3.View balance')
    print('4.Exit')
    ch=input('Enter choice : ')

    if ch=='1':
        obj.deposit(float(input('Enter amount to deposit: ')))

    elif ch=='2':
        obj.withdraw(float(input('Enter amount to withdraw: ')))
    elif ch=='3':
        print('Balance is : ',obj.b)
    elif ch=='4':
        exit()
    else:
        print('Wrong choice')

