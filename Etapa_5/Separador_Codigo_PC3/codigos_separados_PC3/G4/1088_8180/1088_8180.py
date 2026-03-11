n1 = float(input(": "))
n2 = float(input(": "))
n3 = float(input(": "))
n4 = float(input(": "))
n5 = float(input(": "))
soma = ((n1 + n2 + n3 + n4 + n5)/5)

if (soma >= 7.0):
	print(round(soma, 2))
	print("Aprovado")
else: 
	print(round(soma, 2))
	print("Reprovado por nota")