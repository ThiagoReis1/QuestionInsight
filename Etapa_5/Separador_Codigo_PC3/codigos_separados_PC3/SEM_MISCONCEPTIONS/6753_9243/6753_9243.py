numero = int(input("Digite o numero: "))
 
if numero == 42:
	mensagem  = ("tesouro")
elif numero < 42:
	mensagem = ("menor")
else:
	mensagem = ("maior")
	
print (mensagem)