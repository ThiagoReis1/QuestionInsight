from math import*
k = float(input("digite um numero: "))
x = int(input("digite um numero: "))
senh = k
f = 0
g = 1
while(f<k):
	senh = senh + (k**(g+2))/factorial(g+2)
	f = f+1
print(round(senh,9))