nascimento = int(input("digite o ano de nascimento: "))
pais = input("digite a letra do pais: ").upper()

var = 2023 - nascimento

if(var >= 18 and pais == "B"):
	print("sim")
	anos =  var - 18
	print(anos)
elif (var >= 21 and pais == "R"):
	print("sim")
	anos = var - 21
	print(anos)
elif (0 < var < 18 and pais == "B"):
	print("nao")
	anos = 18 - var
	print(anos)
elif (0 < var < 21 and pais == "R"):
	print("nao")
	anos = 21 - var
	print(anos)
else:
	print("invalido")