ko= input("k ou o: ")
valor = float(input("Qual o valor: "))

if(ko=='K'):
	
	Oz=35.274*valor
	print(round(Oz,2))
else:
	k= (valor/35.274)
	print(round(k,2))