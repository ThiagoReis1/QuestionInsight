x = int(input("digite um numero: "))

if (x % 37 == 0):
	mensagem = "sim"
	Q = (x // 37)
	print(Q)
	print(mensagem)

else:
	mensagem = "nao"
	Q = (x % 37)
	print(Q)
	print(mensagem)