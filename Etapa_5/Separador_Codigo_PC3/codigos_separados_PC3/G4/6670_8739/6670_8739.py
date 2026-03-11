from numpy import*

precos = array(eval(input("preco: ")))
i = 0
soma = 0
q = 0
while i < size(precos):
	if (precos[i])> 20:
		soma = soma + precos[i]
		q+=1
	i += 1
	
if q == 0:
	print(0.0)
else:
	print(round(soma/q,2))
