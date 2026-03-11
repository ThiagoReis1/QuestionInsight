#Oxigenio 
O = 15.9994
#Carbono 
C = 12.011
#Nitrogenio 
N = 14.00674
#Hidrogenio 
H = 1.00794

# Peso Alanina
PA = (C*3 + H*7 + N + O*2)
#peso valina
PV = C*5 + H*11 + N + O*2

palavra = input("".upper())

if(palavra == "ALANINA"):
	print(round(PA, 2))
else:
	print(round(PV, 2))