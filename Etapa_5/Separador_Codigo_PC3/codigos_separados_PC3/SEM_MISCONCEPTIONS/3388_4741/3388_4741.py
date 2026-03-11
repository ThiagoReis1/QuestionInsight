unid=input("unidade de energia:")
valor=float(input("valor da medida:"))
if(unid=="W"):
	btu=3.41214*valor
	print(round(btu,2))
if(unid=="B"):
	watthora=valor/3.41214
	print(round(watthora,2))
