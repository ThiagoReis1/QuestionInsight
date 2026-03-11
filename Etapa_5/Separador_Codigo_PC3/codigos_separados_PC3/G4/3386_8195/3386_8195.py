var = input("unidade de medida (R/G): ")
VAR2 = float(input("valor do angulo: "))

if(var == "R"):
	rad = VAR2/0.0174533
else:
	rad = 0.0174533*VAR2
print(round(rad,2))