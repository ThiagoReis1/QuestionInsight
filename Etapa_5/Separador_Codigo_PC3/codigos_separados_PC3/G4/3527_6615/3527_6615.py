from math import*
x = float(input("digite um numero: "))
k = int(input("digite a quantidade de series: "))
i = 0
e = 0
while(i<k):
	e = e + (x**i)/factorial(i)
	i = i + 1
print(round(e,9))