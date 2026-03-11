from math import *
x= float( input("valor de x:"))
k= int(input("valor de k:"))
i=0
e=0
while(k > i):
	e= e + (x**(i)) / factorial(i)
	i= i + 1
print(round(e,9))