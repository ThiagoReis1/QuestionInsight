from numpy import *
dano = array(eval(input("Digite o dano: ")))
i = 0
soma = 0
while(i<size(dano)):
	soma = soma + dano[i]*(i+1)
	i = i + 1
print(soma)