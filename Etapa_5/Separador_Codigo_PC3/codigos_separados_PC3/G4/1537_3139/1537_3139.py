from math import*
x = float(input("numero real: "))
k = int(input("qunatidade de termos em serie: "))

soma = 0
cont = 0

while(cont < k):
	d = factorial(cont)
	soma = soma + x**(cont)/d
	cont = cont + 1
	
print(round(soma, 9))
	
	


	
	
	
