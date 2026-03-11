from math import *

x = float(input())
k = int(input())

mac = 1
cont = 1
n = 2 

while(cont < k):
	cosh = (x ** n)/factorial(n)
	mac = mac + cosh
	cont = cont + 1
	n = n + 2
	
print(round(mac,8))	
