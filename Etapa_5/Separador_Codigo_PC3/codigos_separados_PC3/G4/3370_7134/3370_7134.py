med = input("unidade:").upper()
tam = float(input("medida:"))

if med == "C":
	res = 0.393701 * tam
else:
	res = tam/0.393701
print(round(res, 2))