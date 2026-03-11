unidade=input("qual a unidade usada A/H ")
valor=float(input("qual a medida a ser convetida "))
if(unidade.upper()=="H"):
	medida=2.47105*valor
else:
	medida=valor/2.47105
print(round(medida,2))
