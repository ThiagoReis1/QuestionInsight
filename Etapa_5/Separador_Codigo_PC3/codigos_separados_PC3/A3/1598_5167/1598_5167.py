from numpy import*

valores = array(eval(input("Informe os custos dos itens: ")))
cont = 0
x = 0
total = 0
while (cont < size(valores)):
	if valores[cont] >= 90:
		x = x + 6.50	
	cont =  cont +1
		
total = sum(valores) - x
print(round(total,2))

	
	

