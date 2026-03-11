pedido= input("se for fatia de bolo ou salgado (B/2): ")
quant= int(input("fatias de bolo ou salgado: "))
quant2= int(input("cappuccinos: "))
fb= 5.00
sal= 4.00
cap= 7.50
if(pedido=="B"):
	form= (fb*quant)+(cap*quant2)
else:
	form= (sal*quant)+(cap*quant2)
print(round(form,2))