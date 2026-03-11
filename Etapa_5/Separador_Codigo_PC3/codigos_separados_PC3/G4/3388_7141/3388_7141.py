u = input("Qual a unidade de medida usada: b ou w? ").upper()
v = float(input("Qual o valor da medida?: "))

if (u == "W"):
     b = 3.41214*v
else:
	b = v/3.41214
	
print(round(b, 2))