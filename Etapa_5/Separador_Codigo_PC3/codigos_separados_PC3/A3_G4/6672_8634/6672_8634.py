from numpy import *
pro = array(eval(input("Preco dos produtos comprados pela cliente: ")))
cont = 0
soma = 0
media = 0
for i in range(size(pro)):
	if pro[i] > 180.0:
		cont+=1
		soma += pro[i]
if cont != 0:
	media = soma/cont
	print(round(media, 2))
else:
	print(0.0)