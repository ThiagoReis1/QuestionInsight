num = int(input())

if num%13 == 0:
	print(num//13)
	mensagem = "sim"
else:
	print(num%13)
	mensagem = "nao"
print(mensagem)