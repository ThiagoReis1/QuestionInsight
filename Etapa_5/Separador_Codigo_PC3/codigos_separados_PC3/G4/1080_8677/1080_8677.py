n1 = float(input("insira a primeira nota: "))
n2 = float(input("insira a segunda nota: "))
n3 = float(input("insira a terceira nota: "))

media = (n1+n2+n3) / 3
print(round(media, 1))

if media >= 5.0:
	print("Aprovado")
else:
	print("Reprovado")
	