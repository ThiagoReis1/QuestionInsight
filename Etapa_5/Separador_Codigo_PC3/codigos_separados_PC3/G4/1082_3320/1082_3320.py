p1=float(input("nota 1:"))
p2=float(input("nota2:"))
p3=float(input("nota3:"))
p4=float(input("nota4:"))
p5=float(input("nota5:"))

media= (p1+p2+p3+p4+p5)/5

if(media>=5):
	print(round(media, 1), "Aprovado")
else:
	print(round(media, 1), "Reprovado")