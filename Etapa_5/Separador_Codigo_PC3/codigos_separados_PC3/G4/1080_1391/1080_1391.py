a1 = float(input("valor da primeira nota: "))
b2 = float(input("valor da segunda nota: "))
c3 = float(input("valor da terceira nota: "))

media = (a1 + b2 + c3) / 3

if (media >= 5):
	print(round(media, 1))
	print("Aprovado")
	
else: 
	print(round(media, 1))
	print("Reprovado")