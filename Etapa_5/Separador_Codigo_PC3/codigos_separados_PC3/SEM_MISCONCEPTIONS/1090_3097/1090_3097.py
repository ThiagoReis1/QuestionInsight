limite=float(input("limite"))
valor1=float(input("valor1"))
valor2=float(input("valor2"))
valor3=float(input("valor3"))
valor4=float(input("valor4"))
condicao=valor1+valor2+valor3+valor4
if(limite>=condicao):
	print(round(condicao,2))
	print("Dentro do limite")
else:
	print(round(condicao,2))
	print("Estourou o limite")