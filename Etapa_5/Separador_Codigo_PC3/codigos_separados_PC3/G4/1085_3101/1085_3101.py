n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))
n5 = float(input("Digite a nota 5: "))

m = (n1 + n2 + n3 + n4 + n5) / 5

if (m >= 6.0):
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao"
	
print(round(m, 2))
print(mensagem)