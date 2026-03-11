p1 = float(input("Prova 1: "))
p2 = float(input("Prova 2: "))
p3 = float(input("Prova 3: "))
p4 = float(input("Prova 4: "))
p5 = float(input("Prova 5: "))

media = (p1 + p2 + p3 + p4 + p5) / 5

if(media >= 5):
	print(round(media, 1))
	print("Aprovado")
	
else:
	print(round(media, 1))
	print("Reprovado")