'''
Encapsulation : Binding data and methods together as a single unit
Access specifiers:
1. Public : (name)
2. Protected : (_name)
3. Private : (__name)
'''
class A:
    a = 10
    _b = 20
    __c = 30
obj = A()
print(obj.a)
print(obj._b)
# print(obj.__c) # gives error
print(obj._A__c) # class name + private specifier

#update a private number
class Bank:
    def __init__(self, balance):
        self.__balance = balance
    def credit(self, amount):
        self.__balance += amount
    def debit(self, amount):
        self.__balance += amount
    def view(self):
        print("Total amount:", self.__balance)
b = Bank(1000)
b.view()
b.credit(1500)
b.debit(500)
b.view()