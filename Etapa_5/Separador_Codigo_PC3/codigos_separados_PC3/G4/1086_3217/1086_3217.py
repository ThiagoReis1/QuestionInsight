u = float(input())
m = float(input())
a = float(input())
k = round((u+m+a)/3, 1)
if (k >= 7.0):
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
print(k)
print(mensagem)