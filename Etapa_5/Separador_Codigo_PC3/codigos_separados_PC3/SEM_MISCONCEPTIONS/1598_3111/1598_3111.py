from numpy import*
VetorCompras = array(eval(input("Preco de cada produto: ")))
ValorTotal = 0;
Tam = size(VetorCompras)
for i in range(Tam):
	ValorTotal += float(VetorCompras[i]) -5.00*(VetorCompras[i] >= 80)
	
	
print(round(ValorTotal,2))

