n = int(input("insira um numero: "))

#saida
d1 = n // 1000
d2 = n %1000

if ((d1+d2)**2 == n):
	mensagem = ("atende")
	print("atende", n)
else: 
	mensagem = ("nao atende")
	print("nao atende", n)