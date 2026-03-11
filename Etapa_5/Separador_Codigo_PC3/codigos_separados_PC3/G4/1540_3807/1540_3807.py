from math import*

ang = eval(input("angulo em radiandos:"))
k = int(input("numero interiro:"))
soma = 0
i = 0
sinal = 1

while (i < k):
	soma = soma + sinal*(ang**(i)/factorial(i * 2))
	i = i + 1
	sinal = sinal * -1
print(round(soma, 6))

	
	

	


