moeda = str(input("Escolha o lado [CARA] ou [COROA]: ")).upper()
cont1 = 0
cont2 = 0

while moeda != "S":
	if moeda == "COROA":
		cont1 = cont1 + 1
		moeda = str(input("Escolha o lado [CARA] ou [COROA]: ")).upper()
	elif moeda == "CARA"	:
		cont2 = cont2 + 1
		moeda = str(input("Esolha o lado [CARA] ou [COROA]: ")).upper()
contador = cont2
print(contador)