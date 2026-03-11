#Jadson Brendo Pantoja dos Santos - 21601585
#Avaliação Parcial 02
#07/07/2016
a = float(input("nota1: "))
b = float(input("nota2: "))
c = float(input("nota3: "))
d = float(input("nota4: "))
e = float(input("nota5: "))
media = (a + b + c + d + e)/5
print(round(media, 1))
if (media >= 5):
	print("Aprovado")
else:
	print("Reprovado")