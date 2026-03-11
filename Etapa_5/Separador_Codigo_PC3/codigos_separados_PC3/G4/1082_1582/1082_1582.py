p1 = float(input("nota1"))
p2 = float(input("nota2"))
p3 = float(input("nota3"))
p4 = float(input("nota4"))
p5 = float(input("nota5"))

media = round((p1+p2+p3+p4+p5)/5 , 1)
print(round(media, 1))
if(media>=5):
	print(("Aprovado"))
else:
	print(("Reprovado"))

