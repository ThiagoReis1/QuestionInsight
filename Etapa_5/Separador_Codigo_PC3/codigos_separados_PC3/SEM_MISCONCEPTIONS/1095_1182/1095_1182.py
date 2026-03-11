n1 = int(input("insira um valor: "))
parte1 = n1 // 10000
parte2 = n1 % 10000
if(n1 == (parte1 + parte2)**2):
	print(n1,"atende a prioridade")
else:
	print((parte1 + parte2)**2)