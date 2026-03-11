n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
ma = round((n1 + n2 + n3) / 3, 1)
print(ma)
if (ma >= 5):
	m = "Aprovado"
else:
	m = "Reprovado"
print(m)