valor = float(input(":"))
codigo = input(":").upper()

if codigo == "P" or codigo == "D":
	total = -17/100
elif codigo == "C1":
	total = valor*0
elif codigo == "C2":
	total =  8/100
	
total1 = (valor * total ) + valor

print(round(total1,2))