a=int(input("numero de equitares: "))

if(a < 10000):
	mensagem=float( a * 5.00)
	
else:
	mensagem=float (a - 10000) *4 + 10000 * 5
	
print( mensagem)
	