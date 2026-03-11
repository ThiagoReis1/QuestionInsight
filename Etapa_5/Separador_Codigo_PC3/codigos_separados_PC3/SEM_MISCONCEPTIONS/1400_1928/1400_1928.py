ataque = input("Informe o tipo de ataque: ")
rodadas = int(input("Quantas rodadas ficou na garra da vinha:"))
d1 = int(input("Valor sorteado no dado1: "))
d2 = int(input("Valor sorteado no dado2: "))
n = d1+d2
constricao = (n+1)*rodadas
polen = d1*d2

if (ataque=="polen"):
	vida = polen
	print(vida)
else:
	vida = constricao
	print(vida)