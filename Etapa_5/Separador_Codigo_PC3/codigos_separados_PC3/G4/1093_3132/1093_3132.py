n = int(input("numero: "))
x = n // 100
y = n % 100
if (x**2 + y**2 == n):
	mensagem = ("atende")
else:
	mensagem = ("nao atende")
print(mensagem)
print(n)