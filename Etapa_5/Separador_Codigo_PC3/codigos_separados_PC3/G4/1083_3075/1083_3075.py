n1 = float(input())
n2 = float(input())
n3 = float(input())

m = (n1 + n2 + n3)/3

if (m >= 6.0):
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao"

print(round(m,2))
print(mensagem)