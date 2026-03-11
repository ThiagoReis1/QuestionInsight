# faça seu código aqui!
pratos = int(input("quantidade de pratos consumidos: "))
var = input("deseja sobremesa(S/N)")

valor = pratos * 40.0 

if (var.upper() == "S"):
	valort = valor - (valor * (5 / 100))
	
else:
	(var.upper() == "N")
	valort = valor 
	
print(valort)
	