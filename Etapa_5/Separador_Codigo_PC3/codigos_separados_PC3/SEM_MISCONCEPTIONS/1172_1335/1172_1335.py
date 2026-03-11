import math
n = int(input("numero de termos: "))
d = 0
k = 1
while (k>=0):
	d=d+(1/factorial(k))
	k = k - 1
print(roun(d,9)