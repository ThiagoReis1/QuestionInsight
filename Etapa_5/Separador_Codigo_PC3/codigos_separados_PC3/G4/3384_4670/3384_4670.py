v1= input("unidade: ")
v2= float(input("valor: "))
if(v1 == "O"):
	m=v2/35.274
	print(round(m, 2))
if(v1 == "K"):
	m=35.274*v2
	print(round(m, 2))