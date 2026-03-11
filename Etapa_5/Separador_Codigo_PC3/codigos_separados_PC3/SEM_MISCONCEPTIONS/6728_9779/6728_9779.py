num=int(input("numero:"))
quo=(num//37)
resto=num%37

if (num%37==0):
	mensagem="sim"
	print(quo)
	print(mensagem)
	
else:
	mensagem="nao"
	print(resto)
	print(mensagem)