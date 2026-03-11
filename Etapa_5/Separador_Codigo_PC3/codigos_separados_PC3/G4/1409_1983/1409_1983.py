ta = input("Tipo de ataque: ")
d1 = int(input("dano 1: "))
d2 = int(input("dano 2: "))
d3 = int(input("dano 3: "))
d4 = int(input("dano 4: "))
espada = ((d1+6)+(d2+6)+(d3+6)+(d4+6))
cauda = (d1+d2+d3)*d4
if(ta == 'espada'):
	print(espada)
else:
	print(cauda)