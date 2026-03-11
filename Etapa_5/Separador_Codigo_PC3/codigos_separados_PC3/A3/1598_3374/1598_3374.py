from numpy import * 

compras = array(eval(input()))

tam = size(compras)
soma = sum(compras)
maior = max(compras)
i = 0
saldo = 0
while i < size(compras):
	if maior > 80:
		saldo=1
	i=i + 1
		
if saldo==1:
	soma=soma - 5.0
		
print(round(soma,2))