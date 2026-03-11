N=int(input("numero inteiro:"))

if N%41==0:
	y=N//41
	print(y)
	mensagem="sim"
	
else:
	x=N%41
	print(x)
	mensagem="nao"
	
	
print(mensagem)