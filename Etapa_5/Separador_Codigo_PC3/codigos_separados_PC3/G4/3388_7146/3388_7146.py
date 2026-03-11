u = input("Digite a unidade em que a medida esta:").upper()
v = float(input("Digite o valor da medida:"))
b = 3.41214 * v
w = v / 3.41214

if (u == "B"):
	print(round(w, 2))
else:
	print(round(b, 2))