n = int (input ("informe um numero: "))

a = n // 1000
b = n % 1000


soma = (a - b)**4
if	(soma == n):
	 mensagem = "atende"
else:
	mensagem = "nao atende"
print (n)
print (mensagem)

