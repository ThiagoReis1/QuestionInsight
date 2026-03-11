x = float (input ("Informe um numero: "))
k = int (input ("Informe o numero de termos: "))
soma = 0
cont = 0
sinal = +1

while	(cont <k):
	soma = soma + sinal*(x**(2*cont+1)/(2*cont+1))
	sinal = -sinal
	cont = cont + 1
print (round (soma, 6))