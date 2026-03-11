quant = input("Palavra: ").upper()
i = 0
cont = 0
for i in range (len(quant)):
	if quant[i] == "c" or quant[i] == "C":
		cont = cont + 1
print(cont)