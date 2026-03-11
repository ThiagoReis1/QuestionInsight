n_1 = float(input("digite a nota_1 : "))
n_2 = float(input("digite a nota_2 : "))
n_3 = float(input("digite a nota_3 : "))
n_4 = float(input("digite a nota_4 : "))

#média aritimética das notas

media = (n_1 + n_2 + n_3 + n_4)/4 

if(media>=6.0):
	print(round(media , 1))
	print("Aprovado") 
else:
	print(round(media , 1))
	print("Reprovado") 
	