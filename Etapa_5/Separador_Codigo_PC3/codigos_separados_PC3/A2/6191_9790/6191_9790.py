moeda = input("c/k? ").upper()
cont = 0

while moeda != 'S':
	if moeda == 'CARA':
		cont = cont + 1
	else:
		#se for coroa
		cont =  cont
	moeda = input("c/k? ").upper()
print(cont)
