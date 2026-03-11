# faça seu código aqui!
quantidade = int(input("quantidade de pratos:"))
caractere = input("s ou n:").upper()
valor = quantidade * 40
if caractere == "s":
	valor = valor - (valor*0.05)
else:
	caractere == "n"
	valor = valor -(valor*0.05)
	
print(round(valor, 2))