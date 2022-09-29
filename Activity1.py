# To demostrate the use of inbuilt functions in python
# len(), abs(), type(), max(), min(), round(), isalnum()

a=12
print(type(a))
a=12.22
print(type(a))
a="hello"
print(type(a))
a="1+2j"
print(type(a))

a=-12
print(abs(a))

a=[1,2,3]
print(len(a))

a=12
b=13
print(max(a,b))

a=12
b=13
print(min(a,b))

a=14.6
print(round(a))

a="hello123"
print(a.isalnum())
