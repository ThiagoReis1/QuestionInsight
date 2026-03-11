nome = input()
nome = nome.upper()

#ARGININA: C6 H15 N4 O2
#TIROSINA: C9 H11 N O3
#TRIPTOFANO: C11 H11 N2 O2

if nome =="ARGININA":
	p = (12.011*6) + (1.00794*15) + (14.00674*4) + (15.9994*2)
	print(round(p, 2))
elif nome =="TIROSINA":
	p = (12.011*9) + (1.00794*11) + (14.00674) + (15.9994*3)
	print(round(p, 2))
elif nome =="TRIPTOFANO":
	p = (12.011*11) + (1.00794*11) + (14.00674*2) + (15.9994*2)
	print(round(p, 2))
else:
	print("Entrada: " + nome)
	print("Dado Invalido")