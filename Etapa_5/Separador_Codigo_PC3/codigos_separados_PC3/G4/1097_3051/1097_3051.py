num=int(input("numero fornecido: "))
n1=num//1000
n2=n1%1000

if (num == (n1-n2)**2):
	print("atende")
else:
	print("nao atende")