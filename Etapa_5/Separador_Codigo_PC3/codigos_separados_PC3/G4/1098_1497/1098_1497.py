#Jadson Brendo Pantoja dos Santos - 21601585
#Avaliação Parcial 02
#07/07/2016
x = int(input("valor: "))
a = x % 1000
b = x // 1000
p = (b - a)**4
if (x == p):
	print(x,"atende a propriedade")
else: 
	print(p)
