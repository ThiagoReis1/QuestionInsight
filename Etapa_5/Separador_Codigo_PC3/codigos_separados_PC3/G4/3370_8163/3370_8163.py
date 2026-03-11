u= str(input("unidade (C/P): ")).upper()
v= float(input("valor da medida: "))


if u=="P":
	x= v/0.393701
else:
	x= 0.393701*v
print(round(x,2))