'''
Inheritance : Acquiring properties from one class to another
Types of Inheritance :
1. Single
2. Multi-level
3. Hierarchical
4. Multiple
5. Hybrid
'''
#Single Inheritance
class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("This is class B display method")
b = B()
b.display1()
b.display2()

#Multi-level Inheritance
class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("This is class B display method")
class C(B):
    def display3(self):
        print("This is class C display method")

#Hirarchical
class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("This is class B display method")
class C(A):
    def display3(self):
        print("This is class C display method")

#Multiple Inheritance
class A:
    def display1(self):
        print("This is class A display method")
class B:
    def display2(self):
        print("This is class B display method")
class C(A, B):
    def display3(self):
        print("This is class C display method")
c = C()
c.display()
#



