x = float(input("Numero real:"))
k = int(input("Quantidade de termos:"))

cont = 0
soma = 0
e = 1

while(cont<k): 
	if(cont%2 == 0):
		n = x**e
		m = n/e
		soma = soma + m
		cont = cont + 1
		e = e + 1
	else:
		n = x**e
		m = n/e
		soma = soma - m
		cont = cont + 1
		e = e + 1
		
print(round(soma, 10))