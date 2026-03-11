from math import*
nome=input("digite o nome da armadura: ")
fator=int(input("digite o fator de destreza: "))
if(nome=="malha"):
	res=15*fator-1
	print(res)
else:
	res=20*fator-18
	print(res)