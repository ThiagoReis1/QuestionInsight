num = int(input("Digite um numero:"))

parte1 = num // 1000
parte2 = num % 1000

if (num == (parte1 - parte2)**4) :
	print(num,"atende a propriedade")
	
else :
	saida = (parte1 - parte2)**4
	print(saida)