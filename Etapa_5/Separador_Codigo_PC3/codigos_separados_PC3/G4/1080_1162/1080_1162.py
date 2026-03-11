p1 = float(input("qual a nota 1: "))
p2 = float(input("qual a nota 2: "))
p3 = float(input("qual a nota 3: "))
media = round(((p1 + p2 + p3) / 3), 1)
if(media >= 5):
	print(media)
	print("Aprovado")
else:
	print(media)
	print("Reprovado")