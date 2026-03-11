nome=input(" Qual eh o nome do ataque: ")
l1=int(input(" Valores sorteados no lado um: "))
l2=int(input(" Valores sorteados no lado dois: "))

FURIA = (10+l2+l1)
GRITO = (6+l2+l1)
TOQUE = ((l1+l2)**2)


if(nome=="FURIA"):
	print(FURIA)
elif(nome=="GRITO"):
	print(GRITO)
elif(nome=="TOQUE"):
	print(TOQUE)
elif((l1<1) or (l1>8) or (l2<1) or (l2>8)):
	print(" Entrada invalida")
elif((nome!=TOQUE) or (nome!=FURIA) or (nome!=GRITO)):
	print(" Entrada invalida")