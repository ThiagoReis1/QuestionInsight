po = int(input("quantidade de pecas de ouro: "))
nome = input("nome da armadura: ").upper()
d = int(input("dado: "))
if(d>0)or(d<8):
		if (po>=200):
			print(30*d-20)
		elif(po>=100):
			print(20*d-18)
		elif(po>=50):
			print(15*d-1)
		elif(po<50 and po<100 and po<200):
			print("PO insuficiente")
else:
	print("Entrada invalida")

	