from numpy import*
v = array(eval(input("Vetor de custo dos itens: ")))
i = 0
soma=0
d = 5

while(i<size(v)):
	soma = soma + v[i]
	i = i + 1

desconto = soma

if(soma > 80):
	desconto = soma - d

print(round(desconto,2))