n1 = float(input("insira a nota 1:"))
n2 = float(input("insira a nota 2:"))
n3 = float(input("insira a nota 3:"))
n4 = float(input("insira a nota 4:"))
n5 = float(input("insira a nota 5:"))

media = (n1 + n2 + n3 + n4 + n5) / 5
print(round(media,1))
if media >= 5:
	print("Aprovado")
else:
	print("Reprovado")