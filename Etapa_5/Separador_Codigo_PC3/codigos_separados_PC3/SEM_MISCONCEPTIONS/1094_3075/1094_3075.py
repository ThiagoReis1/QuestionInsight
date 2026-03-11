n = int(input())

n2 = (n//1000 + n%1000)**2
if (n2 == n):
	mensagem = "atende"
else:
	mensagem = "nao atende"
print(mensagem)
print(n)