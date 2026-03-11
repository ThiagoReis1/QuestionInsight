hora = int(input())
qtd = int(input())

conta = qtd*28.50

if( hora >= 18):
	conta -= conta * 0.2
	
print(conta)
