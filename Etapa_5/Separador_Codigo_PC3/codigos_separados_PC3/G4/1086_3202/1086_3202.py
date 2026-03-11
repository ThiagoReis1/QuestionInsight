a = float(input())
b = float(input())
c = float(input())

x = (a + b + c)/3

if (x >= 7.0):
	mensagem = "Aprovado"
else:
	mensagem= "Reprovado"
print(round(x,1))
print(mensagem)