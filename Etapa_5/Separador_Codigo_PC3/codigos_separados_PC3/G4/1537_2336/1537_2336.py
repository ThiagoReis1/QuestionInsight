from math import*
x = int(input("Digite X: ")) 
k = int(input("Digite K: "))

cont = 1
e = 0
n = 0
while(cont < k):
	e = e +(x**cont)/factorial(n)
	n = n+1
	cont = cont + 1
print(round(e,9))