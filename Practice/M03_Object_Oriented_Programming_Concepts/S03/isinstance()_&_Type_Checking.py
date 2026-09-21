'''
type checking = it mainly used to check the object/ value it belongs to particular class
'''
a = 10
b = 15.5
c = "Ram"
d = [1,2,3,4,5,6]
e = (1,2,3,10,45,6)
f ={1,2,3,4,5,6}
g = {"name" : "ananya"}
print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, str))
print(isinstance(d, list))
print(isinstance(e, list))
print(isinstance(f, set))
print(isinstance(g, dict))

x = "Ram"
if isinstance(x,(int,float)):
    print("x is a number")
else:
    print("x is a string")

#checking of object's class
class A:

class B(A):

b = B()
print(isinstance(b, A))
print(isinstance(b, B))


#how they ask in interviews
class A:

class B(A):

obj = B()
print(type(obj) == B)
print(type(obj) == A)
print(isinstance(obj, B))
print(isinstance(obj, A))
