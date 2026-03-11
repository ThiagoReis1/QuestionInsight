#LEIA: A COR DA CASA
#S SEJA LIDO 
#SAIDA: QUANTAS VEZES A BOLA CAIU NA CASA PRETA

cor = input("Digite a cor da casa (PRETA/VERMELHA): ")

p = 0
v = 0

while( cor.upper() != "S"):
	if( cor.upper() == "PRETA"):
		p = p + 1
		cor = input("Digite a cor da casa (PRETA/VERMELHA): ")
	else:
		v = v + 1
		cor = input("Digite a cor da casa (PRETA/VERMELHA): ")
print(p)













