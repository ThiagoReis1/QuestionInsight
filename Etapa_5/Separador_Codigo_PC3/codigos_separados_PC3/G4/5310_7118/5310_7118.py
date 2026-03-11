from math import*

x = float(input())
k = int(input())

cont = 0
acum = 0
i = 1

while (cont < k):
	acum = acum + (x / factorial (i))
	i = i + 2
	cont = cont + 1
print(round(acum , 8))





