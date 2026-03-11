from math import *
x= float(input("digite o numero real:"))
k= int(input("digite a quantidade:"))

i=1
c=0

while (i <= k):
	c= c + x ** (2 * i - 1)/ factorial(2 * i - 1)
	i= i + 1

print(round(c,9))