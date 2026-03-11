ataque = (input("Qual tipo de ataque a vitima sofreu? "))
rodadas = int(input("Informe o numero de rodadas que o personagem permaneceu nas vinhas"))
d1 = int(input("Qual falor sorteado em d1? "))
d2 = int(input("Qual falor sorteado em d2? "))

if (ataque.lower() == "constricao"):
	n = d1+d2
	a = n+1
	dano = (a *rodadas)
	
if (ataque.lower() == "polen"):
	dano = d1*d2
print (dano)