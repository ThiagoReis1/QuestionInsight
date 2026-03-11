from math import*
x = float(input("x"))
k = int(input("k"))
pos = 0
cont = 0
acm = 0 
while (pos<k):
	z = x**cont/factorial(cont) 
	pos = pos +1
	cont = cont + 2
	acm = acm + z

print((round(acm,8)))