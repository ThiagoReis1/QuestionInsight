a = float(input("Avaliacao1: "))
b = float(input("Avaliacao2: "))
c = float(input("Avaliacao3: ")) 
media = (a + b + c) / 3
print(round(media, 1))

if(media >= 5):
	print("Aprovado")
else:
	print("Reprovado")