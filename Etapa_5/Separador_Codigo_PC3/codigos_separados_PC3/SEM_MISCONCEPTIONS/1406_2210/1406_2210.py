
atta=(input("entre com atta: "))
valor=int(input("dado: "))
turnos=int(input("turnos: "))


if(atta=="cauda"):
	dano=valor*turnos
	print(dano)
else:
	dano=2*valor*turnos
	print(dano)


