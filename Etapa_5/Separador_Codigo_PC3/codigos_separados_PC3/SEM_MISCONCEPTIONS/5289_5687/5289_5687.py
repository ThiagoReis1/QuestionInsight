Dado = int(input("digite a face: "))
cont_total = 0 
cont6 = 0

while (Dado != -1): 
	cont_total = cont_total + 1
	if (Dado == 6):
		cont6 = cont6 + 1
	Dado = int(input("digite a face: "))
print(cont_total)
print(round(cont6/cont_total*100,2))





