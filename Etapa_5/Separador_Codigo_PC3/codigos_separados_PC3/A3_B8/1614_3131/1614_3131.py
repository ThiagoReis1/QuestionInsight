from numpy import *

alimentos = input("Nome dos alimentos: ").upper()
calorias = array(eval(input("Caloria dos alimentos: ")))

banana = 0.97
bife = 2.95
feijoada = 1.27
omelete = 1.04
tomate = 0.2

i = 0
i1 = 0
i2 = 0
i3 = 0
i4 = 0

cont = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

while (i < len(alimentos)):
	if (alimentos[i] == "BANANA"):
		cont = cont + 1
		i = i + 1
	elif(alimentos[i] == "BIFE"):
		cont1 = cont1 + 1
		i1 = i + 1
	elif(alimentos[i] == "FEIJOADA"):
		cont2 = cont2 + 1
		i2 = i + 1
	elif(alimentos[i] == "OMELETE"):
		cont3 = cont3 + 1
		i3 = i + 1
	elif(alimentos[i] == "TOMATE"):
		cont4 = cont4 + 1
		i4 =  i + 1
	
total = ((cont * calorias[i]) * banana) + ((cont1 * calorias[i1]) * bife) + ((cont2 * calorias[i2]) * feijoada) + ((cont3 * calorias[i3]) * omelete) + ((cont4 * calorias[i4]) * tomate)
print(total)