po=int(input("pecas de ouro:"))
nome=input("armadura:").upper
d= int(input("destreza: "))
if(po<0 and po>=8):
	if(po>=200 and nome=="INTEIRA"):
		print((30*d)-20)
	elif(po<200 and nome=="INTEIRA"):
		print("PO insuficiente")
	elif(po>=50 and nome=="MALHA"):
		print((15*d)-1)
	elif(po<50 and nome=="MALHA"):
		print("PO insuficiente")
	elif(po>=200 and nome=="PLACA"):
		print((20*d)-18)
	elif(po<200 and nome=="PLACA"):
		print("PO insuficiente")
else:
	print("Entrada invalida")