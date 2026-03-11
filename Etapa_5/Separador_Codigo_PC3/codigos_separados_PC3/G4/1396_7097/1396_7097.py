#Entrada de variaveis
vc=float(input("digete o valor consumido:"))
#Variavel vc=valor consumido
if vc<=300: 
	print(round(vc*(10/100)+vc,2))
else:
	print(round(vc*(6/100)+vc,2))