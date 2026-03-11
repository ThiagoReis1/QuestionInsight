from numpy import*
vci = array(eval(input("vetor de custos dos itens:")))
sum(vci)
i=0

while(i>=80):
	i = i+1
	i = i*(15/100)
soma = sum(vci)
print(round(soma, 2))