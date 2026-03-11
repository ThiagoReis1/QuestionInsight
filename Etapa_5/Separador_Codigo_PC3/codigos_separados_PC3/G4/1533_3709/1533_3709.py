from math import*
x = int(input("numero inteiro: "))
n = int(input("o tal numero natural: "))
v = 0 #variavel contadora
so = 0 #numero que vou usar pra somar
k = 0 #variavel acumuladora
eq = 1
while (v < n):
	k = k + eq
	so = so + 2
	eq = (x ** so) / factorial(so) 
	v = v + 1
print(round(k, 8))