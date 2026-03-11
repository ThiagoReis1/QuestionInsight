ar=(input("digite o nome da armadura: "))
fd=int(input("fator destreza: "))

if (ar=="malha"):
	destreza=((15*fd)-(1))
	print(destreza)
else:
	destreza=((20*fd)-(18))
	print(destreza)