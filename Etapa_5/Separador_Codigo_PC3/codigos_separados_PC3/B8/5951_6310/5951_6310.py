pedido = input()
qnt = int(input())
qntAcai = int(input())
total = 0
if(pedido.upper() == 'T'):
	total += qnt*4.5 + qntAcai*12
elif(pedido.upper() == 'S'):
	total += qnt*5.0 + qntAcai*12
print(round(total,2))