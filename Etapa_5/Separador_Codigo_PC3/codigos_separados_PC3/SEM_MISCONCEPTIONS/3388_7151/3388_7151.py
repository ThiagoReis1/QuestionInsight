unidade= input("unidade")
valor = float(input("valor da medida"))

if unidade=="B":
	total= (valor/3.41214)
else:
	total=(3.41214*valor)
	
print(round(total,2))
	
	


	
	


