q = int(input("Quantidade de PO: "))
nome = input("Armadura(INTEIRA,MALHA,PLACA): ")
d = int(input("Numero de destreza: "))

if (q<100) and (nome=="PLACA") or (q<200) and (nome=="INTEIRA") or (q<50) and (nome=="MALHA"):
	print("PO insuficiente")
elif(d>8) or (d<1):
	print("Entrada invalida")
elif(nome == "INTEIRA"): 
	ft = (30*d)-20
	print(ft)
elif(nome == "MALHA"):
	ft = (15*d)-1
	print(ft)
elif(nome == "PLACA"):
	ft = (20*d)-18
	print(ft)
