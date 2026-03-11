cenouras = int(input('insira o numero de cenouras: '))

if cenouras < 5:
	total = (cenouras * 1.20)
else:
	total = (cenouras * 0.90)
	
print (round(total,2))