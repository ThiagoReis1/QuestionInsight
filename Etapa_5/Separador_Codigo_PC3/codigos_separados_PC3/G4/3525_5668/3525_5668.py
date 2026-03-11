import math
x = float(input("numero x: "))
k = int(input("numero de termos: "))
n = 1
n2 = 1
v = 0
while(n2 <= k):
	f = x ** n / math.factorial(n)
	n = n + 2
	n2 = n2 + 1
	v = f + v

print(round(v, 9))