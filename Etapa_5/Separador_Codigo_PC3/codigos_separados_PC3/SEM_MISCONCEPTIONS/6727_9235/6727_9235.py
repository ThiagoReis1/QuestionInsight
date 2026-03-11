x = int(input("digite o numero: "))

if(x%31 == 0):
	c = x//31
	mensagem = ("sim")
	
else:
	c = x%31
	mensagem = ("nao")
	
print(c)
print(mensagem)