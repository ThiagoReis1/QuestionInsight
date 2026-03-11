X = int(input("Qual o valor do numero ?"))
p1 = X // 100
p2 = X%100
calculo = p1 ** 2 + p2 ** 2
if( X == calculo) :
	print("X atende a propriedade")
else:
	print (calculo)