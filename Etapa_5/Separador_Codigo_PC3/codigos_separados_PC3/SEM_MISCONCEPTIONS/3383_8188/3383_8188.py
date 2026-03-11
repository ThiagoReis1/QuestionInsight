medida=input("qual a medida ").upper()
valor=float(input("qual o valor "))
calculo1=2.20462*valor
calculo2=valor/2.20462

if medida=="L":
	print(round(calculo2,2))

else:
	print(round(calculo1,2))

