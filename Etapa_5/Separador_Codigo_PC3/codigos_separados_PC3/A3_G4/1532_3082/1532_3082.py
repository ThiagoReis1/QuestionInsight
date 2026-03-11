from math import *
x = float(input("um numero real: "))
k = int(input("numero da sequencia: "))
e = 1
l = k-1
while(e < k):
	e = 1+(2*l)
	a =(x**e)/factorial(e)	
print(e)