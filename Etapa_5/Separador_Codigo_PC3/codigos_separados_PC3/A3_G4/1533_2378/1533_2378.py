from math import*

x = float(input("insira x: "))
k = int(input("insira k: "))
i = 0
cosx = x

while(i < k):
	cosx = 1 + x**i/factorial(k)
	i = i+2

print(round(cosx, 8))