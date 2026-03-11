from numpy import *

dado = array(eval(input("Valor dado: ")))
i = 0
calculo = 0
total = 0

while i < size(dado):
	if dado[i] == 1:
		total = 100.0 
		calculo = calculo + total
		total = 100.0
	if dado[i] == 2:
		total = total + (total * 2)
		calculo = calculo + total
		total = 100.0
	if dado[i] == 3:
		total = total + (total / 3)
		calculo = calculo + total
		total = 100.0
	if dado[i] == 4:
		total = total + (total * 4)
		calculo = calculo + total
		total = 100.0
	if dado[i] == 5:
		total = total + (total / 5)
		calculo = calculo + total
		total = 100.0
	if dado[i] == 6:
		total = total + (total * 6)
		calculo = calculo + total
		total = 100.0
	i = i + 1
print(round(calculo, 2))

	