a1=float(input("nota 1: "))
a2=float(input("nota 2: "))
a3=float(input("nota 3: "))
a4=float(input("nota 4: "))

media=(a1+a2+a3+a4)/4

if (media)>=7:
	m=round(media,2)
	r="Aprovado"
	print(m)
	print(r)
else:
	m=round(media,2)
	r="Reprovado"
	print(m)
	print(r)
	