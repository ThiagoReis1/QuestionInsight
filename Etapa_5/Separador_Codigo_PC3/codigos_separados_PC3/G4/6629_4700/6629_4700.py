# faça seu código aqui!
ent = input("Digite a string: ").upper()
i = 0
cont = 0
tam = len(ent)
while (i < tam):
	if (ent[i]=="P"):
		print (i)
		cont = cont + 1
	i = i+1
if (cont == 0):
	print("nao achei")