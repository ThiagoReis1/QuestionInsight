n = int(input("numero fornecido: "))
d1 = n//100
d2 = n%100
dx = (d1**2)+(d2**2)
if (dx==n):
	mensagem=("atende")
else:
	mensagem=("nao atende")
print(mensagem)
print(n)