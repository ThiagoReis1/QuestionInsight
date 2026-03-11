from numpy import *

n= array(eval(input("vetor de custo: ")))

i =0
desconto =0
while(i < size(n)):
	if(n[i]<80):
		desconto= desconto + n[i] *0.15
	i= i + 1
	desconto= sum(n)
print(round(desconto,2))
