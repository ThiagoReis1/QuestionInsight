NA=input("Nome da Armadura:")
FD=int(input("Fator de Destreza:"))

if(NA=="malha"):
	print(int(15*FD-1))
else:
	print(int(20*FD-18))