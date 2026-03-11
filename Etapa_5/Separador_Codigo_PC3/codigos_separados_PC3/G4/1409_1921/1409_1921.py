from math import*
ataque = input("qual ataque a ser usado: ").lower()
a = int(input("primeiro valor sorteado: "))
b = int(input("primeiro valor sorteado: "))
c = int(input("primeiro valor sorteado: "))
d = int(input("primeiro valor sorteado: "))
if(ataque == "espada"):
	p = 6 + a
	pontos = p*4
	print(pontos)
if(ataque == "cauda"):
	k = (b + c + a)*d
	print(k)