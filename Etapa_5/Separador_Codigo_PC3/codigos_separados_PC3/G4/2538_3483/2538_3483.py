s=int(input("digite o valor do sitio: "))
d=int (input("digite o valor inicial: "))
m= int (input("depositos mensais: "))
j= (input("taxa de juros: "))
mes=0
while s > 0:
	meses = s- (d + m* (j / 100))
	mes = mes + 1

print (round(meses,2))