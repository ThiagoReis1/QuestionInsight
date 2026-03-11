armadura= input("digite o nome da armadura:")
f_destreza= int(input(" numero de 1 a 8:"))

if	(armadura =='placas'):
	resistencia=20*f_destreza-18
	print(int(resistencia))
if (armadura=='malha'):
	resistencia= 15*f_destreza -1
	print(int(resistencia))