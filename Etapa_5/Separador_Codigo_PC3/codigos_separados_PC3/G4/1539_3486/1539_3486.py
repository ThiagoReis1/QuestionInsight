x = float(input('digite um numero real:'))
k = int(input('quantidade de termos:'))

a = 0 
soma = 0
sinal = +1
while (a < k): 
	
	soma = soma +sinal*(x**a) 
	sinal = -sinal
	a = a + 1

print(round(soma, 7))