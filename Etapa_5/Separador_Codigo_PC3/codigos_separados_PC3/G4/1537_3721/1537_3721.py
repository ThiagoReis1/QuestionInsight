from math import*
x= float(input("Digite um numero: "))
k= int(input("Digite um numero: "))
ct= 0
ae= 0
n= 0
pot= 0 
while ct<k:
	e= (x**pot)/(factorial(n))
	ae= ae + e
	pot= pot+1
	ct= ct+1
	n= n+1

print(round(ae,9))