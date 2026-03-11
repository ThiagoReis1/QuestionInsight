unidade_da_medida = input("R/G:")
U = float(input("angulo:"))

if unidade_da_medida == "R":
	CONVERSAO = U/0.0174533
else:
	CONVERSAO = 0.0174533*U
print(round(CONVERSAO,2))