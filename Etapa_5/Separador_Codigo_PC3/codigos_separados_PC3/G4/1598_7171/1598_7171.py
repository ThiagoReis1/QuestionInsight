#descontos
from numpy import*
ct= array(eval(input("Digite o vetor custo:")))

i=0
desc=0

while (i<size(ct)):
	if (ct[i]>90):
		desc= desc + 6.5
	else: 
		desc= desc+ 0
	i=i+1
custo= sum(ct)-desc
print(round((custo),2))

	