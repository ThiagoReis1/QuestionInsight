p1 = float(input("digite o valor de p1: "))
p2 = float(input("digite o valor de p2: "))
p3 = float(input("digite o valor de p3: "))
media = (p1+p2+p3)/3
if media>=5:
	m=round(media,1)
	a="Aprovado"
	print(m)
	print(a)

else:
	m=round(media,1)
	a="Reprovado"
	print(m)
	print(a)
