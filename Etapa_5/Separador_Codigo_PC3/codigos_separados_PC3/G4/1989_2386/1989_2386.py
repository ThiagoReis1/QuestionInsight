#Oxigenio 
O = 15.999
#Carbono 
C = 12.011
#Nitrogenio
N = 14.00674
#Hidrogenio 
H = 1.00794
#Pesos
PA = 4 * C + 8 * H + 2 * N + 3 * O
PG = 5 * C + 8 * H + 1 * N + 4 * O
PT = 11 * C + 11 * H + 2 * N + 2 * O

Entrada = input("")
Aminoacido = Entrada.upper()

if(Aminoacido == "ASPARAGINA"):
	print(round(PA, 2))
elif(Aminoacido == "GLUTAMINA"):
	print(round(PG, 2))
elif(Aminoacido == "TRIPTOFANO"):
	print(round(PT, 2))
else:
	print("Entrada:", Aminoacido)
	print("Dado Invalido")