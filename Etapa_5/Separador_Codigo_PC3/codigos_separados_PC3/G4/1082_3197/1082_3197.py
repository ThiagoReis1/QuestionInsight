p1 = float(input())
p2 = float(input())
p3 = float(input())
p4 = float(input())
p5 = float(input())
media = (p1+p2+p3+p4+p5)/5
if (media >= 5):
	mensagem = ("Aprovado")
	print(round(media, 1))
	print(mensagem)
else:
	mensagem = ("Reprovado")
	print(round(media, 1))
	print(mensagem)