valor = float(input())
cod = input()

cod = cod.upper()

if cod == "D":
	valor = valor - valor * 0.12
elif cod == "P":
	valor = valor * 0.12
elif cod == "C1":
	valor = valor 
elif cod == "C2":
	valor = valor + valor * 0.07
	
print(round(valor, 2))