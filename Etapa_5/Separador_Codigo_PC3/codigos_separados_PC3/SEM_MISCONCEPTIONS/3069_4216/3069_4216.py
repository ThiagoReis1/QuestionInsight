n  = input("Nome do ataque: ")
v1 = int(input("Valor1: "))
v2 = int(input("Valor2: "))

if(1<=v1<=8)and(1<=v2<=8):
	if(n.upper()=="FURIA"):
		e = 10+(v1+v2)
		print(e)
	elif(n.upper()=="GRITO"):
		e = 6+(v1+v2)
		print(e)
	elif(n.upper()=="TOQUE"):
		e = (v1+v2)**2
	else:
else:
	print("Entrada Invalida")

