from numpy import*

custo = array(eval(input("Custo dos intens:"))) 

cont = 0
total = 0

while cont < size(custo):
	if custo [cont] > 90:
		total = total + (custo[cont] - 6.5)
	else:
		total = total + (custo[cont] + 0)
	cont = cont + 1
	
print(round(total,2))