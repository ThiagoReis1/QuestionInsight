p1 = float(input("qual a nota 1: "))
p2 = float(input("qual a nota 2: "))
p3 = float(input("qual a nota 3: "))
p4 = float(input("qual a nota 4: "))
media = ((p1 + p2 + p3 + p4) / 4)
print(round(media, 2))
if (media >= 7):
	print("Aprovado")
else:
	print("Reprovado")
	