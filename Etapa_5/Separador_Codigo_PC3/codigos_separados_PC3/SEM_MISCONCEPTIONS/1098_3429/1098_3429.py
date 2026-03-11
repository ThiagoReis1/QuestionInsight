a = int(input("Digite o valor aqui"))

conta=a//1000
conta2=a%1000
conta3=(conta-conta2)**4
if(conta3 == a):
	print(a)
	print("atende")
else:
	print(a)
	print("nao atende")
	