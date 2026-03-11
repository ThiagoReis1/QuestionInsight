cidade = input("cidade: ")
idade = int(input("idade: "))

print("Entradas:",cidade, ",",idade)

vpv = 500.00
vs = 370.00
vb = 600.00
vt = 360.00
vta = 550.00
d1 = 30/100 * 500
d2 = 30/100 * 370
d3 = 30/100 * 600
d4 = 30/100 * 360
d5 = 30/100 * 550

if idade <= 2 and idade >= 0 and cidade == "Porto Velho" and cidade == "Santarem" and cidade == "Belem" and cidade == "Tefe" and cidade == "Tabatinga":
	print("Passagem:", "R$", "0" )
elif idade >= 3 and idade <= 12 and cidade == "Porto Velho":
	valor = vpv / 2
	print("Passagem:", "R$", valor)
elif idade >= 3 and idade <= 12 and cidade == "Santarem":
	valor = vs / 2
	print("Passagem:", "R$", valor)
elif idade >= 3 and idade <= 12 and cidade == "Belem":
	valor = vb / 2
	print("Passagem:", "R$", valor)
elif idade >= 3 and idade <= 12 and cidade == "Tefe":
	valor = vt / 2
	print("Passagem:", "R$", valor)
elif idade >= 3 and idade <= 12 and cidade == "Tabatinga":
	valor = vta / 2
	print("Passagem:", "R$", valor)
elif idade > 12 and idade < 65 and cidade == "Porto Velho":
	print("Passagem:", "R$", vpv)
elif idade > 12 and idade < 65 and cidade == "Santarem":
	print("Passagem:", "R$", vs)
elif idade > 12 and idade < 65 and cidade == "Belem":
	print("Passagem:", "R$", vb)
elif idade > 12 and idade < 65 and cidade == "Tefe":
	print("Passagem:", "R$", vt)
elif idade > 12 and idade < 65 and cidade == "Tabatinga":
	print("Passagem:", "R$", vta)
elif idade >= 65 and idade < 150 and cidade == "Porto Velho":
	valor = vpv - d1
	print("Passagem:", "R$", valor)
elif idade >= 65 and idade < 150 and cidade == "Santarem":
	valor = vs - d2
	print("Passagem:", "R$", valor)
elif idade >= 65 and idade < 150 and cidade == "Belem":
	valor = vb - d3
	print("Passagem:", "R$", valor)
elif idade >= 65 and idade < 150 and cidade == "Tefe":
	valor = vt - d4
	print("Passagem:", "R$", valor)
elif idade >= 65 and idade < 150 and cidade == "Tabatinga":
	valor = vta - d5
	print("Passagem:", "R$", valor)
elif idade > 150 or idade < 0 or (cidade != "Porto Velho" and cidade != "Santarem" and cidade != "Belem" and cidade != "Tefe" and cidade != "Tabatinga"):
	print("entradas invalidas")


	