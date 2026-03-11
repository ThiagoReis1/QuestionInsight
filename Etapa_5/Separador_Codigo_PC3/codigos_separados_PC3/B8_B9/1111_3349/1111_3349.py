n1 = float(input("Insira a nota 1: "))
n2 = float(input("Insira a nota 2: "))
n3 = float(input("Insira a nota 3: "))
n4 = float(input("Insira a nota 4: "))
n5 = float(input("Insira a nota 5: "))
media = (n1 + n2 + n3 + n4 + n5) / 5
x = media
if(x >= 5.0):
	print(round(x,1))
	print("Aprovado")
else:
	print(round(x,1))
	print("Reprovado")