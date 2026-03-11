nota_a = float(input("digite nota A:")) 
nota_b = float(input("digite nota B:")) 
nota_c = float(input("digite nota C:")) 
nota_d = float(input("digite nota D:"))

media = ((nota_a + nota_b + nota_c + nota_d)/4)
if (media >= 6):
	print(round(media , 1))
	print("Aprovado")
else:
	print(round(media , 1))
	print("Reprovado")
