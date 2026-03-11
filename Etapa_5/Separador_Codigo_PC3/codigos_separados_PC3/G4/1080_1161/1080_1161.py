p1 = float(input("insira uma nota: "))
p2 = float(input("insira uma nota: "))
p3 = float(input("insira uma nota: "))
media = round(((p1+p2+p3)/3), 1)
if(media >=5):
	print(media)
	print("Aprovado")
else:
	print(media)
	print("Reprovado")