parcial_1 = float(input("Digite a parcial_1: "))
parcial_2 = float(input("Digite a parcial_2: "))
parcial_3 = float(input("Digite a parcial_3: "))

nota_final = (parcial_1 + parcial_2 + parcial_3)/3

if (nota_final >= 5):
	noticia = ("Aprovado")
else:
	noticia = ("Reprovado")
	
print(round(nota_final, 1))
print(noticia)