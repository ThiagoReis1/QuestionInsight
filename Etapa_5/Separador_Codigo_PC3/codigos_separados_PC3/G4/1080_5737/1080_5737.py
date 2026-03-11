n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

m = (n1 + n2 + n3) / 3

if(m >= 5):
	print(round(m,1))
	print("Aprovado")
else:
	print(round(m,1))
	print("Reprovado")

