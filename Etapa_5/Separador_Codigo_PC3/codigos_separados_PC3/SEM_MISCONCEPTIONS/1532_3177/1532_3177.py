x = float(input("digite"))
k = int(input("digite"))
cont = 1
soma = 0
while(cont>0):
	if(cont==1):
		 x = x + (x**3/(factorial(3)) + x**5/(factorial(5)) +  x**7/(factorial(7)) + (cont))
	      soma = soma + x
	else:
		x = x + (x**3/(factorial(3) + x**5/(factorial(5)) +  x**7/(factorial(7)) + (cont)) 
	cont = cont + 1
print(round(soma,9))	