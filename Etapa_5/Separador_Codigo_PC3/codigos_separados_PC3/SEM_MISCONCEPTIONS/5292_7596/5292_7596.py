s = input("escreva a cor: ").upper()
PRETA = 0
VERMELHA = 0
cont = 0

while (s != "S"):
	if (s == "PRETA"):
		PRETA = PRETA + 1
	else:
		VERMELHA = VERMELHA + 1
	cont = cont + 1
	s = input("escreva a cor: ").upper()
if(cont > 0):
	valor = PRETA / cont * 100
	print(cont)
	print(round(valor,2))