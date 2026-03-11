from numpy import*
x=array(eval(input("Coloque o vetor compras:")))
soma=0
for i in range(size(x)):
	if x[i] > 80:
		x[i] = x[i] - 5.0
	soma = soma + x[i]
print(round(soma, 2))