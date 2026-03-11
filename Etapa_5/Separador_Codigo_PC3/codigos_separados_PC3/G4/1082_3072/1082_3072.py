n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))
n4 = float(input("nota 4: "))
n5 = float(input("nota 5: "))

m = (n1 + n2 + n3 + n4 + n5) / 5

if (m >= 5):
	mensagem = "Aprovado"
	print(round(m,1))
	print(mensagem)
else:
	mensagem = "Reprovado"
	print(round(m,1))
	print(mensagem)	