class A:
    def _s(Self):
        print('A')
class B:
    def _s(Self):
        print('B')
def k(Shape):
    Shape.s()
a = A()
b = B()
print(k(a))
print(k(b))