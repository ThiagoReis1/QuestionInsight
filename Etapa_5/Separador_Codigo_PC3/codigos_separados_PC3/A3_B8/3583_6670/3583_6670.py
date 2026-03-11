from numpy import *

preco=array(eval(input()))

i=0
novo_preco=0
desconto=preco[i]*8/100
while i < size(preco):
	if preco[i]>50:
		novo_preco=preco[i]-desconto
	elif preco[i]<=50:
		novo_preco=sum(mnovo_preco+preco[i])
	i+=1
print(round(novo_preco,2))