print("Digite as 5 notas")
p1 = float(input())
p2 = float(input())
p3 = float(input())
p4 = float(input())
p5 = float(input())
media = round(((p1+p2+p3+p4+p5)/5), 1)
if(media >= 5):
	print(media)
	print("Aprovado")
else:
	print(media)
	print("Reprovado")