p1 = float(input("nota da primeira prova: "))
p2 = float(input("nota da segunda prova: "))
p3 = float(input("nota da terceira prova: "))
p4 = float(input("nota da quarta prova: "))
p5 = float(input("nota da quinta prova: "))

media = (p1 + p2 + p3 + p4 + p5)/5
if(media >= 6):
	print(round(media,2))
	print("Aprovado")
else:
	print(round(media,2))
	print("Reprovado")