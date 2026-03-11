n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))

m = (n1+n2+n3)/3

print(round(m, 1))

if (m >= 7):
	print("Aprovado")
else:
	print("Reprovado")

