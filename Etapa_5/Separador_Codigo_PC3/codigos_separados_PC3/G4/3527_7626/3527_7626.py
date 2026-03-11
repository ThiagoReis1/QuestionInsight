from math import*
x= float(input(""))
k= float(input(""))

c=0
soma=0

while c != k:
	tem= (x**c)/ factorial(c)
	soma= soma + tem
	c = c + 1
print(round(soma, 9))
