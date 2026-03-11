p1 = float(input("digite media p1: "))
p2 = float(input("digite media p2: "))
p3 = float(input("digite media p3: "))
p4 = float(input("digite media p4: "))
p5 = float(input("digite media p5: "))

media = (p1 + p2 + p3 + p4 + p5)/5
print(round(media, 2))
if (media >= 6.0):
	print("Aprovado")
else:
	print("Reprovado")

