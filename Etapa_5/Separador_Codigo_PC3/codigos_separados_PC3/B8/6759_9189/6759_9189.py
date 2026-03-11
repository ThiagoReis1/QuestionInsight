# faça seu código aqui!
dis = int ( input ("digite a distancia inteira em km: "))

tax = 50.00

if dis < 10:
	total = tax + 5.50
	print (round(total,2))

elif dis == 10:
	total = tax + 7.75
	print (round(total,2))
	
elif dis> 10:
	total = tax + 10.00
	print (round(total,2))