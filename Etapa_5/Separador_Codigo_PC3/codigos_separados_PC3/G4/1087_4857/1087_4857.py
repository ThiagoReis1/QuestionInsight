a = float(input("Digita a N1: "))
b = float(input("Digite a N2: "))
c = float(input("Digite a N3: "))
d = float(input("Digite a N4: "))

m = (a+b+c+d)/4
if (m >= 7):
	print(round(m,2),"Aprovado")
else:
	print(round(m,2), "Reprovado")