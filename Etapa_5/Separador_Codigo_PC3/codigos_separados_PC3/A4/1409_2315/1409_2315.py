ataque=input("nome do ataque")
dado1=int(input("dado 1: "))
dado2=int(input("dado 2: "))
dado3=int(input("dado 3: "))
dado4=int(input("dado 4: "))
if(ataque=="espada"):
	dano=(dado1+dado2+dado3)*dado4
	print=(dano)
if (ataque=="cauda"):
	dano=((dado1+dado2+dado3+dado4)+24)
	print(dano)