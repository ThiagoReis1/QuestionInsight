o = float(input("Quantidade de pecas de ouro: "))
n = input("Nome da armadura(MALHA, PLACA ou INTEIRA): ")
d = int(input("Fator de destreza(1 a 8): "))

if(n=="INTEIRA") and (200<=o) and (0<d) or (d<9):
	r1 = int((30*d) -20)
	print(r1)
elif(o<200):
	print("PO insuficiente")
elif(n!="INTEIRA") or (0>d) or (d>8):
	print("Entrada insuficiente")
elif(n=="MALHA") and (50<=o) and (0<d) or (d<9):
	r2 = int((15*d)-1)
	print(r2)
elif(o<50):
	print("PO insuficiente")
elif(n!="MALHA") or (0>d) or(d>8):
	print("Entrada invalida")
elif(n=="PLACA") and (100<=o) and (0<d) or (d<9):
	r3 = int((20*d) -18)
	print(r3)
elif(o<100):
	print("PO insuficiente")
elif(n!="PLACA") or (0>d) or (d>8):
	print("Entrada invalida")
else:
	print("Entrada invalida")

	