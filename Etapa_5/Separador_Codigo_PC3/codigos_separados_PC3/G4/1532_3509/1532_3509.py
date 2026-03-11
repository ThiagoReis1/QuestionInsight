from math import*
x = float(input("numero real:"))
k = int(input("Digite outro termo:"))
i = 0
e = 0
while(i<k):
	e = e + (x**(2*i+1)/factorial(2*i+1))
	i = i + 1
print(round(e,9))
