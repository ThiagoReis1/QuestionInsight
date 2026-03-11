from numpy import *
itens=array(eval(input("custo do item:")))

i=0
desconto=0
while (i<size(itens)):
	if (itens[i]> 50.0):
		desconto= desconto+itens[i] * 0.08
	i+=1

soma=sum(itens)-desconto
print(round(soma,2))
	