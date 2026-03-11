a = float(input())
b = float(input())
c = float(input())

m = (a + b + c) / 3

if (m >= 5):
	print(round(m,1))
	print("Aprovado")
else:
	print(round(m,1))
	print("Reprovado")