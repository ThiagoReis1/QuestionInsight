p1 = float(input("nota 1: "))
p2 = float(input("nota 2: "))
p3 = float(input("nota 3: "))
p4 = float(input("nota 4: "))
media = (p1+p2+p3+p4)/4
if(media >= 6.0):
	media = (p1+p2+p3+p4)/4
	men ="Aprovado"
	print(round(media,1))
	print(men)
else:
	media = (p1+p2+p3+p4)/4
	men = "Reprovado"
	print(round(media,1))
	print(men)
	