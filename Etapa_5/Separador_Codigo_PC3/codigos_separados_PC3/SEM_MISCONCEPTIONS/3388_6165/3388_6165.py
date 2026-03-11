u = input("Qual a unidade de medida usada: b ou w:? ").upper()

v = float(input("Qual o valor da medida?: "))

if (u == "W"):
	conversao = 3.41214*v
else:
	 conversao = v/3.41214

print(round(conversao, 2))