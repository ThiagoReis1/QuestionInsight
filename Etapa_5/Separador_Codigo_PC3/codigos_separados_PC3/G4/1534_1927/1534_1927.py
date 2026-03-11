x = float(input("nmr x"))
k = int(input("nmr k"))
soma = 0
i = 1
sinal = -1
if(k==1):
	soma = soma +1
	print(round(soma,7))
else:
	while(i<=k):
		soma = soma + (sinal*(x**i))
		sinal = -sinal
		i = i+1
		k=k+1
	print(float(round(soma,7)))
