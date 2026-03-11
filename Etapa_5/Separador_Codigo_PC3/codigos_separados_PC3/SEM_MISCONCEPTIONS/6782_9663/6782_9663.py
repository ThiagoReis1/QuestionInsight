idade=int(input("igite o valor do seu ano de nascimento:"))
pais = input("Digite B para Brasil e E para Estados Unidos: ").upper()

i2 = 2023 - idade

if pais == "B" and i2 >= 18:
	print("sim")
	f = i2 - 18
	print(f)

	print("nao")
	ii = 18-i2
	print(ii)
if pais == "E" and i2 >= 16:
	print("sim")
	total = i2 - 16
	print(total)
else:
	print("nao")
	total2= 16 - i2
	print(total)
elif pais != "B" and "E":
	print("invalido")
	