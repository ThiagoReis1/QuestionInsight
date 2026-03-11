variavel = int(input("numero:"))
n1 = variavel//10000
n2 = (variavel%10000)//100
n3 = (variavel%10000)%100

if(variavel==(n1**3+n2**3+n3**3)):
	print("atende")
	print(variavel)
else:
	print("nao atende")
	print(variavel)
	