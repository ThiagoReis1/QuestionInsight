
valor = float(input("insira: "))
c = input("insira ").upper()

if(c == "D"):
	total = valor -valor*0.12
elif(c == "P"):
	total= valor - valor*0.12
elif ( c == "C1"):
		total = valor
else:
	total = valor + valor*0.07
	
print(round(total,2))	