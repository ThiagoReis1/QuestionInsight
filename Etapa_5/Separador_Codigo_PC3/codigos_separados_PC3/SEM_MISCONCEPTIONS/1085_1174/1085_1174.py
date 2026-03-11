notaA = float(input("Digite a: "))
notaB = float(input("Digite b: "))
notaC = float(input("Digite c: "))
notaD = float(input("Digite d: "))
notaE = float(input("Digite e: "))

media = round(((notaA + notaB + notaC + notaD + notaE) / 5), 2)	
if (media >= 6.0):
	print(round(media, 2))
	print("Aprovado")
else:
	print(round(media, 2))
	print("Reprovado")