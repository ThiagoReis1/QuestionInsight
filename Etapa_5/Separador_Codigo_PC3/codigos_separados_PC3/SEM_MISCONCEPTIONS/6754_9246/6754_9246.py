numero = int(input("digite numero:"))

if numero == 175:
	mensagem = ("premiado")
elif numero < 175:
	mensagem = ("menor")
else:
	mensagem = ("maior")
	
print (mensagem)