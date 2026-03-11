
v = float(input(""))
v1 = float(input(""))
v2 = float(input(""))
v3 = float(input(""))
v4 = float(input(""))
m = (v + v1 + v2 + v3 + v4) / 5

if(m >= 5.0):
	print(round(m, 1))
	print("Aprovado")
else:
	print(round(m, 1))
	print("Reprovado")
	