p = float(input("BogoMips do processador: "))

cont1 = 7208.14
cont2 = 2018

while cont1 < p:
	cont2 += 1
	cont1 = (cont1 * 0.65) + cont1
print(cont2)	
