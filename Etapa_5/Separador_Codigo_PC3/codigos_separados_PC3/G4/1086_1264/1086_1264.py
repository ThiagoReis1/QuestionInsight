n1=float(input("Digite a nota 1: "))
n2=float(input("Digite a nota 2: "))
n3=float(input("Digite a nota 3: "))

media= (n1+n2+n3)/3

if (media>= 7):
	a="Aprovado"
else:
	a="Reprovado"
print(round(media,1))
print(a)
	