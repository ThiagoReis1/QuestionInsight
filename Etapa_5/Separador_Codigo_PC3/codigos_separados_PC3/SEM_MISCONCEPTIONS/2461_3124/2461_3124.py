preco = float(input())

if(preco>0 and preco<=50.00):
	valor = preco + 100/100*preco
elif(preco>=50.01 and preco<=100.00):
	valor = preco + 50/100*preco
elif(preco>=100.01 and preco<=500.00):
	valor = preco + 40/100*preco
else:
	valor = preco + 30/100*preco
print(round(valor,2))
	
	