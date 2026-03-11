n1 = float(input("nota 1:"))
n2 = float(input("nota 2:"))
n3 = float(input("nota 3:"))

media = (n1 + n2 + n3) / 3

if(media >= 5):
	print(round(media, 1), "Aprovado") 
else:
	print(round(media, 1), "Reprovado")
