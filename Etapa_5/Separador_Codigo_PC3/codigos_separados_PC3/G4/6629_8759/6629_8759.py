from numpy import*
# faça seu código aqui!
i=0
u=0
nome= str(input())
while i< len(nome):
	if nome[i].upper() == "P":
		print(i)
		u=u+ 1
	i= i + 1
if u==0:
	print("nao achei")