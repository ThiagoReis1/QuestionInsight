nota_1= float(input("nota 1"))
nota_2= float(input("nota 2"))
nota_3= float(input("nota 3"))
nota_4= float(input("nota 4"))

soma= (nota_1+nota_2+nota_3 +nota_4)/4
print(round(soma,2))

if soma >= 7.0:
	print("Aprovado")
else:
	print("Reprovado")

