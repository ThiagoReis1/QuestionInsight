x = int(input("valor de x:"))

if x % 31 == 0:
	resultado = x//31
	mensagem = "sim"
	
else:
	resultado = x % 31
	mensagem = "nao"
	
print(resultado)
print(mensagem)
	