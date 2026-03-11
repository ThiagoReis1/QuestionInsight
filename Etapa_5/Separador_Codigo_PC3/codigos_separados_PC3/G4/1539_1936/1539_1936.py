x = float(input("valor de x: "))
k = int(input("termos: "))
soma = 1
i = 1
sinal = -1
if(k==1):
	print(float(round(soma,7)))
else:
	while(i<k):
		soma = soma +(sinal*(x**i))
		sinal = -sinal
		i = i+1
		
		
print(float(round(soma,7)))