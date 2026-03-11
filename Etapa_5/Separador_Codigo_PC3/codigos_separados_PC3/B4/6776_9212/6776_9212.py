ano = int(input("qual o ano de nascimento:"))
pais = input("qual o pais:")

if pais.upper() == "B": 
	valor = ano - 2023
	print("nao")
	print(valor)
elif pais == "B" and valor < 21:
	valor = ano - 21
	print("nao")
	print(valor)

elif pais.upper() == "R":
	valor = ano - 2023
	print("nao")
	print(valor)
elif pais == "R" and valor < 18:
	valor = i - 18
	print("nao")
	print(valor)

	
else:
	print("invalido") 
