from math import*
x = float(input("numero real: "))
k = int(input("numero k: "))
cont = 0
e = 0
while(cont<k):
	e = e + 1**cont*x**(cont)/factorial(cont)
	cont=cont+1
print(round(e,9))
